from bokeh.plotting import figure, show, curdoc
from bokeh.models import NumeralTickFormatter
from bokeh.models import HoverTool
from bokeh.models import ColumnDataSource
from bokeh.layouts import widgetbox, column
from bokeh.models import BoxAnnotation
from bokeh.layouts import layout
from bokeh.models import Slider
from matplotlib import colors
import pandas as pd
import numpy as np

# CAPEX GRAPH
####################################
# Get the current slider values
a = 40000000
b = 300000000
c = 250000000
d = 160000000
e = 250000000

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
phover = HoverTool(
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
           tools=[TOOLS, phover])


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
eng_slider = Slider(start=0, end=150000000,
                    value=40000000, step=5000000, title="Engineering")
equip_slider = Slider(start=100000000, end=400000000,
                      value=300000000, step=5000000, title="Equipment")
bulk_slider = Slider(start=100000000, end=400000000,
                     value=250000000, step=5000000, title="Bulk_Materials")
indi_slider = Slider(start=10000000, end=310000000,
                     value=160000000, step=5000000, title="Indirects")
lab_slider = Slider(start=100000000, end=400000000,
                    value=250000000, step=5000000, title="Labour")

# PAYBACK GRAPH
####################################


# Data
Oil_Price = 45
Fuel = 3
Opp_Cost = 10
Sus_Cap = 8
Royalties = 7
Taxes = 2.8
Emission_Comp = 0.3
Transport = 6
Other = 1
Uptime = 0.95
Net = Uptime * (365 * (40000 * (Oil_Price - (Fuel + Opp_Cost +
                                             Sus_Cap + Royalties + Taxes + Emission_Comp + Transport + Other))))
Year = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
        16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]


# Return Calculation
y0 = -et / 2
y1 = -et / 2
y2 = Net / 3
y3 = Net / 2
y4 = Net / 1.5
y5 = Net
y6 = Net
y7 = Net
y8 = Net
y9 = Net
y10 = Net
y11 = Net
y12 = Net
y13 = Net
y14 = Net
y15 = Net
y16 = Net
y17 = Net
y18 = Net
y19 = Net
y20 = Net
y21 = Net
y22 = Net
y23 = Net
y24 = Net
y25 = Net
y26 = Net
y27 = Net
y28 = Net
y29 = Net
y30 = Net


# Payback data list
Payback = [y0, y0 + y1, y0 + y1 + y2, y0 + y1 + y2 + y3, y0 + y1 + y2 + y3 + y4, y0 + y1 + y2 + y3 + y4 + y5, y0 + y1 + y2 + y3 + y4 + y5 + y6,
           y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7, y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8, y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 +
           y8 + y9, y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 +
           y10, y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 + y10 + y11,
           y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 + y10 + y11 + y12, y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 +
           y8 + y9 + y10 + y11 + y12 + y13, y0 + y1 + y2 + y3 + y4 +
           y5 + y6 + y7 + y8 + y9 + y10 + y11 + y12 + y13 + y14,
           y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 + y10 + y11 + y12 + y13 + y14 + y15, y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 +
           y10 + y11 + y12 + y13 + y14 + y15 + y16, y0 + y1 + y2 + y3 + y4 + y5 +
           y6 + y7 + y8 + y9 + y10 + y11 + y12 + y13 + y14 + y15 + y16 + y17,
           y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 + y10 + y11 + y12 + y13 + y14 + y15 + y16 + y17 + y18, y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 + y10 + y11 +
           y12 + y13 + y14 + y15 + y16 + y17 + y18 + y19, y0 + y1 + y2 + y3 + y4 + y5 + y6 +
           y7 + y8 + y9 + y10 + y11 + y12 + y13 + y14 + y15 + y16 + y17 + y18 + y19 + y20,
           y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 + y10 + y11 + y12 + y13 + y14 + y15 + y16 + y17 + y18 + y19 + y20 + y21, y0 +
           y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 + y10 + y11 + y12 +
           y13 + y14 + y15 + y16 + y17 + y18 + y19 + y20 + y21 + y22,
           y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 + y10 + y11 + y12 + y13 + y14 + y15 + y16 + y17 + y18 + y19 + y20 + y21 + y22 + y23, y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 + y10 + y11 + y12 + y13 +
           y14 + y15 + y16 + y17 + y18 + y19 + y20 + y21 + y22 + y23 + y24, y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 +
           y8 + y9 + y10 + y11 + y12 + y13 + y14 + y15 + y16 +
           y17 + y18 + y19 + y20 + y21 + y22 + y23 + y24 + y25,
           y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 + y10 + y11 + y12 + y13 + y14 + y15 + y16 + y17 + y18 + y19 + y20 + y21 + y22 + y23 + y24 + y25 + y26, y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 + y10 + y11 + y12 + y13 + y14 + y15 +
           y16 + y17 + y18 + y19 + y20 + y21 + y22 + y23 + y24 + y25 + y26 + y27, y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 +
           y9 + y10 + y11 + y12 + y13 + y14 + y15 + y16 + y17 + y18 +
           y19 + y20 + y21 + y22 + y23 + y24 + y25 + y26 + y27 + y28,
           y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 + y10 + y11 + y12 + y13 + y14 + y15 + y16 + y17 + y18 + y19 + y20 + y21 + y22 + y23 + y24 + y25 + y26 + y27 + y28 + y29, y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 + y10 + y11 + y12 + y13 + y14 + y15 + y16 + y17 + y18 + y19 + y20 + y21 + y22 + y23 + y24 + y25 + y26 + y27 + y28 + y29 + y30]


# New sources
returnsource = ColumnDataSource(dict(x=Year, y=Payback))


# HoverTool Label
Thover = HoverTool(
    tooltips=[
        ('Return', '@y{$ 0.00 a}'),
    ]
)


# Other Tools
TOOLS = 'box_zoom, box_select, resize, reset'


# Plot
T = figure(title="Return On Investment", title_location="above",
           plot_width=800, plot_height=400, tools=[TOOLS, Thover])
T.line(x='x', y='y', color="teal", line_width=4,
       alpha=0.75, source=returnsource)


# Format
T.yaxis[0].formatter = NumeralTickFormatter(format="$0,000")
T.add_layout(BoxAnnotation(bottom=0, fill_alpha=0.1, fill_color='teal'))
T.add_layout(BoxAnnotation(top=0, fill_alpha=0.1, fill_color='red'))
T.xgrid.grid_line_color = None
T.ygrid.grid_line_color = 'whitesmoke'


# Set up widgets
oil_slider = Slider(start=20, end=100,
                    value=45, step=5, title="Oil Price")
fuel_slider = Slider(start=0, end=10,
                     value=3, step=1, title="Fuel Cost")
opp_slider = Slider(start=1, end=20,
                    value=10, step=1, title="Operating Cost")
sust_slider = Slider(start=1, end=20,
                     value=8, step=1, title="Sustaining Capital Cost")
roy_slider = Slider(start=0, end=20,
                    value=7, step=1, title="Royalties")
tax_slider = Slider(start=0, end=10,
                    value=2.8, step=0.2, title="Taxes")
emiss_slider = Slider(start=0, end=10,
                      value=0.3, step=0.1, title="Emission Compliance")
tran_slider = Slider(start=0, end=10,
                     value=6, step=1, title="Transport Cost")
oth_slider = Slider(start=0, end=20,
                    value=1, step=1, title="Other Cost")
upt_slider = Slider(start=0, end=1,
                    value=0.95, step=0.01, title="Uptime")


# UPDATE FUNCTION
####################################
def update_data(attrname, old, new):
    # capex function
    ################################

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

    # capex function
    ################################
    # Data - Get current slider value
    Oil_Price = oil_slider.value
    Fuel = fuel_slider.value
    Opp_Cost = opp_slider.value
    Sus_Cap = sust_slider.value
    Royalties = roy_slider.value
    Taxes = tax_slider.value
    Emission_Comp = emiss_slider.value
    Transport = tran_slider.value
    Other = oth_slider.value
    Uptime = upt_slider.value
    Net = Uptime * (365 * (40000 * (Oil_Price - (Fuel + Opp_Cost +
                                                 Sus_Cap + Royalties + Taxes + Emission_Comp + Transport + Other))))
    Year = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
            16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

    # Return Calculation
    y0 = -et / 2
    y1 = -et / 2
    y2 = Net / 3
    y3 = Net / 2
    y4 = Net / 1.5
    y5 = Net
    y6 = Net
    y7 = Net
    y8 = Net
    y9 = Net
    y10 = Net
    y11 = Net
    y12 = Net
    y13 = Net
    y14 = Net
    y15 = Net
    y16 = Net
    y17 = Net
    y18 = Net
    y19 = Net
    y20 = Net
    y21 = Net
    y22 = Net
    y23 = Net
    y24 = Net
    y25 = Net
    y26 = Net
    y27 = Net
    y28 = Net
    y29 = Net
    y30 = Net

    # Payback data list
    Payback = [y0, y0 + y1, y0 + y1 + y2, y0 + y1 + y2 + y3, y0 + y1 + y2 + y3 + y4, y0 + y1 + y2 + y3 + y4 + y5, y0 + y1 + y2 + y3 + y4 + y5 + y6,
               y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7, y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8, y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 +
               y8 + y9, y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 +
               y10, y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 + y10 + y11,
               y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 + y10 + y11 + y12, y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 +
               y8 + y9 + y10 + y11 + y12 + y13, y0 + y1 + y2 + y3 + y4 +
               y5 + y6 + y7 + y8 + y9 + y10 + y11 + y12 + y13 + y14,
               y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 + y10 + y11 + y12 + y13 + y14 + y15, y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 +
               y10 + y11 + y12 + y13 + y14 + y15 + y16, y0 + y1 + y2 + y3 + y4 + y5 +
               y6 + y7 + y8 + y9 + y10 + y11 + y12 + y13 + y14 + y15 + y16 + y17,
               y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 + y10 + y11 + y12 + y13 + y14 + y15 + y16 + y17 + y18, y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 + y10 + y11 +
               y12 + y13 + y14 + y15 + y16 + y17 + y18 + y19, y0 + y1 + y2 + y3 + y4 + y5 + y6 +
               y7 + y8 + y9 + y10 + y11 + y12 + y13 + y14 + y15 + y16 + y17 + y18 + y19 + y20,
               y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 + y10 + y11 + y12 + y13 + y14 + y15 + y16 + y17 + y18 + y19 + y20 + y21, y0 +
               y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 + y10 + y11 + y12 +
               y13 + y14 + y15 + y16 + y17 + y18 + y19 + y20 + y21 + y22,
               y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 + y10 + y11 + y12 + y13 + y14 + y15 + y16 + y17 + y18 + y19 + y20 + y21 + y22 + y23, y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 + y10 + y11 + y12 + y13 +
               y14 + y15 + y16 + y17 + y18 + y19 + y20 + y21 + y22 + y23 + y24, y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 +
               y8 + y9 + y10 + y11 + y12 + y13 + y14 + y15 + y16 +
               y17 + y18 + y19 + y20 + y21 + y22 + y23 + y24 + y25,
               y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 + y10 + y11 + y12 + y13 + y14 + y15 + y16 + y17 + y18 + y19 + y20 + y21 + y22 + y23 + y24 + y25 + y26, y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 + y10 + y11 + y12 + y13 + y14 + y15 +
               y16 + y17 + y18 + y19 + y20 + y21 + y22 + y23 + y24 + y25 + y26 + y27, y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 +
               y9 + y10 + y11 + y12 + y13 + y14 + y15 + y16 + y17 + y18 +
               y19 + y20 + y21 + y22 + y23 + y24 + y25 + y26 + y27 + y28,
               y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 + y10 + y11 + y12 + y13 + y14 + y15 + y16 + y17 + y18 + y19 + y20 + y21 + y22 + y23 + y24 + y25 + y26 + y27 + y28 + y29, y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 + y10 + y11 + y12 + y13 + y14 + y15 + y16 + y17 + y18 + y19 + y20 + y21 + y22 + y23 + y24 + y25 + y26 + y27 + y28 + y29 + y30]

    # New sources
    returnsource.data = dict(x=Year, y=Payback)


for w in [eng_slider, equip_slider, bulk_slider, indi_slider, lab_slider,
          oil_slider, fuel_slider, opp_slider, sust_slider, roy_slider,
          tax_slider, emiss_slider, tran_slider, oth_slider, upt_slider]:
    w.on_change('value', update_data)

#  CAPEX Set up layouts and add to document
inputs = widgetbox(eng_slider, equip_slider,
                   bulk_slider, indi_slider, lab_slider)


# PAYBACK Set up layouts and add to document
Tinputs1 = widgetbox(oil_slider, fuel_slider,
                     opp_slider, sust_slider, roy_slider)

Tinputs2 = widgetbox(tax_slider, emiss_slider,
                     tran_slider, oth_slider, upt_slider)

l = layout([
    [inputs, Tinputs1, Tinputs2],
    [p, T],
], sizing_mode='stretch_both')


# Show!
curdoc().add_root(l)
curdoc().title = "SAGD CAPEX"
