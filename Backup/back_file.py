import folium
import pandas as pd
from sqlalchemy import create_engine

# Подключаемся к базе данных
db_path = "gis_data.db"
engine = create_engine(f"sqlite:///{db_path}")

# Загружаем маркеры и линии улиц
df_markers = pd.read_sql("SELECT street, latitude, longitude, coverage, height, ground FROM markers", engine)
df_streets = pd.read_sql("SELECT street, latitude, longitude, htmlcode FROM streets", engine)

# Создаем карту
m = folium.Map(
    location=[53.722279, 91.443704],
    zoom_start=16,
    tiles=None,
    attribution_control=0
)

# Добавляем слои
folium.TileLayer('CyclOSM', name="CyclOSM").add_to(m)
folium.TileLayer('Esri.WorldImagery', name="Esri World Imagery").add_to(m)
folium.TileLayer('OpenStreetMap', name="OpenStreetMap").add_to(m)

# Функция для определения цвета маркера
def get_marker_color(proj_cover, grass_height):
    if proj_cover < 70 or grass_height > 0.5:
        return "red"
    elif 70 <= proj_cover <= 80 or (0.3 < grass_height <= 0.5):
        return "orange"
    elif proj_cover > 80 and grass_height <= 0.3:
        return "green"
    return "gray"

# Группируем данные по улицам
for street_name in df_markers["street"].unique():
    street_group = folium.FeatureGroup(name=street_name)

    # Добавляем маркеры
    street_markers = df_markers[df_markers["street"] == street_name]
    for _, row in street_markers.iterrows():
        color = get_marker_color(row["coverage"], row["height"])
        folium.Marker(
            location=[row["latitude"], row["longitude"]],
            popup=f"<b>Проективное покрытие:</b> {row['coverage']}%<br/>"
                  f"<b>Высота газона:</b> {row['height']} cм.<br/>"
                  f"<b>Почва:</b> {row['ground']}",
            icon=folium.Icon(icon="seedling", prefix="fa", color=color),
        ).add_to(street_group)

    # Добавляем PolyLine с HTML-попапом
    street_line = df_streets[df_streets["street"] == street_name][["latitude", "longitude"]].values.tolist()
    html_popup = df_streets[df_streets["street"] == street_name]["htmlcode"].iloc[0] if not df_streets[df_streets["street"] == street_name].empty else "Нет данных"

    if street_line:
        folium.PolyLine(
            locations=street_line,
            color="#ff5200",
            weight=5,
            tooltip=street_name,
            popup=folium.Popup(html_popup, max_width=300)  # Добавляем HTML в попап
        ).add_to(street_group)

    # Добавляем группу улицы на карту
    street_group.add_to(m)

folium.LayerControl().add_to(m)

legend_html = """
<div style="
    position: fixed;
    bottom: 50px;
    left: 50px;
    width: 220px;
    background: white;
    z-index:9999;
    font-size:14px;
    border-radius: 10px;
    padding: 10px;
    box-shadow: 2px 2px 5px rgba(0,0,0,0.3);
">
    <b>Легенда</b>
    <br>
    <i class="fa fa-circle" style="color:green"></i> Отличное состояние <br>
    <i class="fa fa-circle" style="color:green"></i> Хорошее состояние <br>
    <i class="fa fa-circle" style="color:orange"></i> Удовлетворительное состояние <br>
    <i class="fa fa-circle" style="color:red"></i> Неудовлетворительное состояние <br>
    <i class="fa fa-circle" style="color:red"></i> Плохое состояние <br>
</div>
"""

m.get_root().html.add_child(folium.Element(legend_html))

# Сохраняем карту
m.save("map.html")

print("Карта успешно сгенерирована! Открывайте map.html")