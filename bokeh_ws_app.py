# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 10:31:00 2019

@author: Emil
"""

import pandas as pd

from bokeh.io import curdoc, output_file, show
from bokeh.plotting import figure
from bokeh.models import OpenURL, TapTool, ColumnDataSource
from bokeh.layouts import column 

output_file('ws_bilbase.html')
df = pd.read_csv(r'C:\Users\Emil\Dropbox\Python sjov\df_uden_leas.csv', sep = ';')

colormap = {'TSi': 'red', 'FSi': 'green', 'TDi': 'blue'}
colors = [colormap[x] for x in df['type']]

df['colors'] = colors

source = ColumnDataSource(df)

plot = figure(x_axis_label = 'KM',y_axis_label = 'Pris',tools="tap")
plot.circle(x='km',y='pris', color='colors', fill_alpha=0.2, size=10,source=source)


url = '@links'

taptool = plot.select(type=TapTool)
taptool.callback = OpenURL(url=url)


layout = column(plot)
# Add the plot to the current document
curdoc().add_root(layout)


show(layout)
