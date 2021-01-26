import csv
import matplotlib.pyplot as plt
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'data/world_fires_1_day.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    lons, lats = [], []
    for row in reader:
        lon = int(row[1])
        lat = int(row[0])
        lons.append(lon)
        lats.append(lat)

data = [{
    'type': 'scattergeo',
    'lon': 'lons',
    'lat': 'lats',
    'marker': {
        'color': "red",
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': '火事の発生地'},
    },
}]
my_layout = Layout(title='世界の火事')
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='grobal_fire.html')
