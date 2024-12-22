import folium

map = folium.Map(
    location=[53.722279, 91.443704],
    zoom_start = 16,
    tiles=None,
    attribution_control=0
)

# слои карты
folium.TileLayer('CyclOSM', name="CyclOSM").add_to(map)
folium.TileLayer('Esri.WorldImagery', name="Esri World Imagery").add_to(map)
folium.TileLayer('OpenStreetMap', name="OpenStreetMap").add_to(map)

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
chertigasheva_coordinates = [
    [53.723706, 91.431490],
    [53.723808, 91.432518],
    [53.724108, 91.435558],
    [53.724206, 91.436697],
    [53.724223, 91.436802],
    [53.724372, 91.437974],
    [53.724412, 91.438316],
    [53.724660, 91.440872],
    [53.724754, 91.441700],
    [53.724843, 91.442738],
    [53.724854, 91.442893],
    [53.724857, 91.442936],
    [53.725037, 91.445045],
    [53.725465, 91.449354],
    [53.725606, 91.450948],
    [53.725824, 91.453085],
    [53.725840, 91.453251],
    [53.725965, 91.454592],
    [53.726027, 91.455169],
]

# линии улиц
html_lenina = '''<h1>Проспект Ленина</h1>
              <img src="https://www.on-walking.com/files/abakan/011.jpg" width="300px" height="200px">  '''
html_shetinkina = '''<h1>Улица Щетинкина</h1>
              <img src="https://i3.photo.2gis.com/main/branch/69/70000001040677149/common" width="300px" height="200px">  '''
folium.PolyLine(
    locations=lenina_coordinates,
    color="#ff5200",
    weight=5,
    tooltip="Проспект Ленина",
    popup=html_lenina,
).add_to(map)
folium.PolyLine(
    locations=shetinkina_coordinates,
    color="#ff5200",
    weight=5,
    tooltip="Улица Щетинкина",
    popup=html_shetinkina,
).add_to(map)
folium.PolyLine(
    locations=krulova_coordinates,
    color="#ff5200",
    weight=5,
    tooltip="Улица Крылова?",
    popup="Улица Крылова?",
).add_to(map)
folium.PolyLine(
    locations=chertigasheva_coordinates,
    color="#ff5200",
    weight=5,
    tooltip="Улица Чертыгашева",
    popup="Улица Чертыгашева",
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
).add_to(map)
folium.Marker(
    location=[53.722445, 91.445457],
    tooltip="Иконка 3",
    popup="Тест3",
    icon=folium.Icon(icon="seedling", prefix="fa", color="orange"), # orange
).add_to(map)

folium.LayerControl().add_to(map)

map.save("map.html")