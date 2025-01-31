import folium
from datamaps import streets

m = folium.Map(
    location=[53.722279, 91.443704],
    zoom_start = 16,
    tiles=None,
    attribution_control=0
)

# слои карты
folium.TileLayer('CyclOSM', name="CyclOSM").add_to(m)
folium.TileLayer('Esri.WorldImagery', name="Esri World Imagery").add_to(m)
folium.TileLayer('OpenStreetMap', name="OpenStreetMap").add_to(m)

# Тестовые маркеры для карты
# folium.Marker(
#     location=[53.721565, 91.436445],
#     tooltip="Иконка 1",
#     popup="Тест1",
#     icon=folium.Icon(icon="seedling", prefix="fa", color="red"),
# ).add_to(m)
# folium.Marker(
#     location=[53.721978, 91.440966],
#     tooltip="Иконка 2",
#     popup="Тест2",
#     icon=folium.Icon(icon="seedling", prefix="fa", color="green"),
# ).add_to(m)
# folium.Marker(
#     location=[53.722445, 91.445457],
#     tooltip="Иконка 3",
#     popup="Тест3",
#     icon=folium.Icon(icon="seedling", prefix="fa", color="orange"), # orange
# ).add_to(m)

for street_name, data in streets.items():
    # Создаем группу для каждой улицы
    street_group = folium.FeatureGroup(name=street_name)

    # Добавляем маркеры
    for marker in data["markers"]:
        folium.Marker(
            location=marker["coords"],
            popup=f"<b>{marker['name']}</b>",
            icon=folium.Icon(icon="seedling", prefix="fa", color="green"),
        ).add_to(street_group)

    # Добавляем линию
    folium.PolyLine(
        locations=data["line"],
        color="#ff5200",  # Цвет линии
        weight=5,      # Толщина линии
        tooltip=street_name,
        popup=data["htmlcode"]


    ).add_to(street_group)

    # Добавляем группу улицы на карту
    street_group.add_to(m)

# Добавляем контроллер слоев для переключения между улицами collapsed=False
folium.LayerControl().add_to(m)
# Сохраняем карту
m.save("map.html")