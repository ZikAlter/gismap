import folium

map = folium.Map(
    location=[53.722279, 91.443704],
    zoom_start = 16, # Мы оставляем эти данные
    tiles = 'OpenStreetmap',
    control_scale=True,
    attribution_control=0
)

# Вот это и оставляем
folium.Marker(
    location=[53.721565, 91.436445],
    tooltip="Иконка 1",
    popup="Тест1",
    icon=folium.Icon(icon="seedling", prefix="fa", color="red"),
).add_to(map)
folium.Marker(
    location=[53.721978, 91.440966],
    tooltip="Иконка 2",
    popup="Тест2",
    icon=folium.Icon(icon="seedling", prefix="fa", color="green"),
).add_to(map) # вот этот маркер оставляем
folium.Marker(
    location=[53.722445, 91.445457],
    tooltip="Иконка 3",
    popup="Тест3",
    icon=folium.Icon(icon="seedling", prefix="fa", color="orange"), # orange
).add_to(map)

map.save("map.html")