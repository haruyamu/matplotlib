import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'data/eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)
all_eq_dicts = all_eq_data['features']
mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

data = [{
    'type': 'scattergeo',
    'lon': 'lons',
    'lat': 'lats',
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'マグニチュード'},
    },
}]
my_layout = Layout(title='世界の地震')

fig = {'data': data, 'layout': my_layout}
offline, plot(fig, filename='grobal_earthquakes.html')
readable_file = 'data/readable_eq_data.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)
