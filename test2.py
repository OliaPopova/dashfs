
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
import numpy
import pylab
# !!! Импортируем класс кнопки и слайдера
from matplotlib.widgets import Button, Slider


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')


x = [1, 2, 3, 4, 5, 6]
y = [6, 7, 8, 9, 10, 11]
x1 = [5, 4, 3, 2, 1]
y1 = [10, 9, 8, 7, 6]
hs3 = go.Bar(name="Экспорт, млн.дол.США", x=x, y=y)
hs4 = go.Bar(name="Импорт, млн.дол.США", x=x1, y=y1)
figure34 = make_subplots(specs=[[{"secondary_y": True}]])
figure34.add_trace(hs4)
figure34.add_trace(hs3)
figure34.update_layout(legend=dict(x=0, y=1.5, traceorder='normal', font=dict(size=12)))



app.layout = html.Div( children=[
    html.H1(children="Дашборд",),
    dcc.Slider(id='prohodnoi_bal',value=0, min=75, max=100, step=1,marks=None),
    dcc.Slider(id='normativi',value=0, min=0, max=20, step=1,marks=None),
    dcc.Slider(id='kolichestvo_mest',value=0, min=0, max=20, step=1,marks=None),
    dcc.Graph(figure=figure34)
    ])

@app.callback(
    Output('graph', 'figure'),
    [Input('prohodnoi_bal', 'value'),
    Input('normativi', 'value'),
    Input('kolichestvo_mest', 'value')])

def update_figure(selected_prohodnoi_bal, selected_normativi, selected_kolichestvo_mest):
    df_bal = df[df.prohodnoi_bal == selected_prohodnoi_bal]
    df_normativi = df[df.normativi == selected_normativi]
    df_kolichestvo_mest = df[df.kolichestvo_mest == selected_kolichestvo_mest]

    hs3 = go.Bar(name="Экспорт, млн.дол.США", x=x, y=y)
    hs4 = go.Bar(name="Импорт, млн.дол.США", x=x1, y=y1)
    figure34 = make_subplots(specs=[[{"secondary_y": True}]])
    figure34.add_trace(hs4)
    figure34.add_trace(hs3)
    figure34.update_layout(legend=dict(x=0, y=1.5, traceorder='normal', font=dict(size=12)))
    return figure34

if __name__ == '__main__':
    app.run_server(debug=True)





