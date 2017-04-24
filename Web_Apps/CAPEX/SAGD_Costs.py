from bokeh.plotting import figure, show, curdoc
from bokeh.models import NumeralTickFormatter
from bokeh.models import HoverTool
from bokeh.models import ColumnDataSource
from bokeh.layouts import widgetbox, column
from bokeh.models import Slider
from matplotlib import colors
import pandas as pd
import numpy as np

# Read Data
df = pd.read_csv('/home/mint/SAGD_Costs.csv')


# Master source
source = ColumnDataSource(df)


# Get the current slider values
a = source.data['Engineering'][0]
b = source.data['Equipment'][0]
c = source.data['Bulk_Materials'][0]
d = source.data['Indirects'][0]
e = source.data['Labour'][0]

# Calculate Top & Bottom
ab = 0
at = a
bb = a
bt = a + b
cb = a + b
ct = a + b + c
db = a + b + c
dt = a + b + c + d
eb = a + b + c + d
et = a + b + c + d + e


# New sources
engsource = ColumnDataSource(data=dict(x=[ab], y=[at], desc=['Engineering']))
equipsource = ColumnDataSource(data=dict(x=[bb], y=[bt], desc=['Equipment']))
bulksource = ColumnDataSource(
    data=dict(x=[cb], y=[ct], desc=['Bulk Materials']))
indisource = ColumnDataSource(data=dict(x=[db], y=[dt], desc=['Indirects']))
labsource = ColumnDataSource(data=dict(x=[eb], y=[et], desc=['Labour']))


# HoverTool Label
hover = HoverTool(
    tooltips=[
        ('Item', '@desc'),
        ('Cost', '@y{$ 0.00 a}'),
    ]
)


# Other Tools
TOOLS = 'box_zoom, box_select, resize, reset'


# Figure
p = figure(title="Capital Costs Breakdown", title_location="above",
           plot_width=600, plot_height=600, x_range=(-2, 2),
           tools=[TOOLS, hover])


# Plots
engbar = p.vbar(x=0, width=2, bottom='x',
                top='y', alpha=0.75, color="darkslategrey",
                legend="Engineering", source=engsource)

equipbar = p.vbar(x=0, width=2, bottom='x',
                  top='y', alpha=0.75, color="teal", legend="Equipment",
                  source=equipsource)

bulkbar = p.vbar(x=0, width=2, bottom='x',
                 top='y', alpha=0.75, color="cyan", legend="Bulk Materials",
                 source=bulksource)

indibar = p.vbar(x=0, width=2, bottom='x',
                 top='y', alpha=0.75, color="powderblue", legend="Indirects",
                 source=indisource)

labbar = p.vbar(x=0, width=2, bottom='x',
                top='y', alpha=0.75, color="lavender", legend="Labour",
                source=labsource)


# Format
p.yaxis[0].formatter = NumeralTickFormatter(format="$0,000")


# Set up widgets
eng_slider = Slider(start=5000000, end=100000000,
                    value=40000000, step=5000000, title="Engineering")
equip_slider = Slider(start=5000000, end=100000000,
                      value=40000000, step=5000000, title="Equipment")
bulk_slider = Slider(start=5000000, end=100000000,
                     value=40000000, step=5000000, title="Bulk_Materials")
indi_slider = Slider(start=5000000, end=100000000,
                     value=40000000, step=5000000, title="Indirects")
lab_slider = Slider(start=5000000, end=100000000,
                    value=40000000, step=5000000, title="Labour")


def update_data(attrname, old, new):

    # Get the current slider values
    a = eng_slider.value
    b = equip_slider.value
    c = bulk_slider.value
    d = indi_slider.value
    e = lab_slider.value

    # Calculate Top & Bottom
    ab = 0
    at = a
    bb = a
    bt = a + b
    cb = a + b
    ct = a + b + c
    db = a + b + c
    dt = a + b + c + d
    eb = a + b + c + d
    et = a + b + c + d + e

    # New sources
    engsource.data = dict(x=[ab], y=[at], desc=['Engineering'])
    equipsource.data = dict(x=[bb], y=[bt], desc=['Equipment'])
    bulksource.data = dict(x=[cb], y=[ct], desc=['Bulk Materials'])
    indisource.data = dict(x=[db], y=[dt], desc=['Indirects'])
    labsource.data = dict(x=[eb], y=[et], desc=['Labour'])


for w in [eng_slider, equip_slider, bulk_slider, indi_slider, lab_slider]:
    w.on_change('value', update_data)


# Set up layouts and add to document
inputs = widgetbox(eng_slider, equip_slider,
                   bulk_slider, indi_slider, lab_slider)


# Show!
curdoc().add_root(column(inputs, p))
curdoc().title = "Sliders"
