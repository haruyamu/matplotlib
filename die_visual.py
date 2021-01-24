from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

die = Die()

results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

x_values = list(range(1, die.num_sides+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': '結果'}
y_axis_config = {'title': '発生した回数'}
my_layout = Layout(title="六面のサイコロを１０００回転がした結果",
                   x_axis=x_axis_config, y_axis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')
