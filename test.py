import numpy
import pylab
import plotly.express as px
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import dash_core_components as dcc
import dash
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
from dash import Dash, dcc, html, Input, Output
from matplotlib import pylab
from pylab import *
# Импортируем класс слайдера
from matplotlib.widgets import Slider
x=[1,2,3,4,5,6,7,8,9,10]
num_steps = len(x)
trace_list = [go.bar(visible=True, x=x, y=x+1, mode='lines+markers', name='f(x)=x<sup>2</sup>')]

for i in range(1, len(x)):
    trace_list.append(
        go.bar(visible=False, x=x*2, y=x+x, mode='lines+markers', name='f(x)=x<sup>2</sup>'))

fig = go.Figure(data=trace_list)

steps = []
for i in range(num_steps):
    # Hide all traces
    step = dict(
        method='restyle',
        args=['visible', [False] * len(fig.data)],
    )
    # Enable trace we want to see
    step['args'][1][i] = True

    # Add step to step list
    steps.append(step)

sliders = [dict(
    steps=steps,
)]

fig.layout.sliders = sliders

fig.show()