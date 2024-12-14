import folium

map = folium.Map(
    location=[53.722279, 91.443704],
    zoom_start = 16, # Мы оставляем zoom
    #tiles = 'OpenStreetMap',
    #control_scale=True,
    attribution_control=0
)

# слои карты
folium.TileLayer('CartoDB.Voyager').add_to(map)
folium.TileLayer('CyclOSM').add_to(map)
folium.TileLayer('Esri.WorldImagery').add_to(map)
folium.TileLayer('OpenStreetMap').add_to(map)

# координаты улиц
lenina_coordinates = [
    [53.7211, 91.4333],
    [53.722755,  91.4495],
    [53.723056, 91.4539],
    [53.7234, 91.4565],
]
shetinkina_coordinates = [
    [53.726186,91.44252],
    [53.734935,91.43993],
    [53.733805,91.440309],
    [53.727508,91.442126],
    [53.7248349,91.442895],
    [53.724819,91.442882],
    [53.722302, 91.44362],
    [53.717319,91.445112],
]
krulova_coordinates = [
    [53.727555, 91.442118],
    [53.727555, 91.442118],
    [53.727828, 91.444923],
    [53.727933, 91.446023],
    [53.727982, 91.447034],
    [53.728177, 91.449259],
    [53.728379, 91.451564],
    [53.728401, 91.451785],
    [53.728714, 91.454590],
]

# линии улиц
# color #FFD30C,#D2B48C,#F0E68C. #ff3300
html_lenina = '''<h1>Проспект Ленина</h1>
              <img src="https://www.on-walking.com/files/abakan/011.jpg" width="150px" height="100px">  '''
html_shetinkina = '''<h1>Улица Щетинкина</h1>
              <img src="https://i3.photo.2gis.com/main/branch/69/70000001040677149/common" width="150px" height="100px">  '''
folium.PolyLine(
    locations=lenina_coordinates,
    color="#F0E68C",
    weight=5,
    tooltip="Проспект Ленина",
    line_cap="square", # предложение
    popup=html_lenina, # предложение добавить popup
).add_to(map)
folium.PolyLine(
    locations=shetinkina_coordinates,
    color="#F0E68C",
    weight=5,
    tooltip="Улица Щетинкина",
    line_cap="square", # предложение
    popup=html_shetinkina, # предложение добавить popup
).add_to(map)
folium.PolyLine(
    locations=krulova_coordinates,
    color="#F0E68C",
    weight=5,
    tooltip="Улица Крылова?",
    line_cap="square", # предложение
    popup="Улица Крылова?", # предложение добавить popup
).add_to(map)

# Тестовые маркеры для карты
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

folium.LayerControl().add_to(map)
map.save("map.html")