
import plotly.express as px
import dash_daq as daq
import dash
from dash import Dash, dcc, html, Input, Output
from foo import foo

import numpy as np
from ipywidgets import Output, VBox
import plotly.express as px
import dash_daq as daq
import dash
from dash import Dash, dcc, html, Input, Output
from foo import foo
import plotly.graph_objects as go


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

app.layout = html.Div( children=[
    html.H1(children="Дашборд",),
    html.Div([
        html.Div(children='''Проходной балл ЕГЭ'''),
        html.Div(children='''Нормативы'''),
        html.Div(children='''Количество бюджетных мест '''),
    ],style = { 'display': 'block','columnCount': 3}),

    html.Div([
            daq.Slider(id='prohodnoi_bal',value=0.75, min=0.75, max=1, step=0.01,marks=None, size=200)],
                       style = {'width': '33%', 'display': 'inline-block'}),
    html.Div([
            daq.Slider(id='normativi',value=0.51, min=0.51, max=1, step=0.01,marks=None, size=200)],
                       style = {'width': '33%', 'display': 'inline-block'}),
    html.Div([
            daq.Slider(id='kolichestvo_mest',value=0.7, min=0.5, max=1, step=0.01,  marks={'25': 'mark', '50': '50'}, size=200)],
                       style = {'width': '33%', 'display': 'inline-block'}),
    dcc.Graph(id='fig1',
              style={'background':'#1d1e1f'}),
    dcc.Graph(id='fig2',
              style={'background': '#1d1e1f'}),
    html.Div(children='''
        Количество обучающихся в классе профильного обучения.
    '''),
    html.Div(children='''
        Информация о факторе.
    '''),
    html.Div(children='''
        Какие показатели влияют на данный фактор.
    ''')
    ]
    )
@app.callback(
    Output('fig1', 'figure'),
    [Input('prohodnoi_bal', 'value'),
    Input('normativi', 'value'),
    Input('kolichestvo_mest', 'value')])

# create our callback function
def update_figure(selected_prohodnoi_bal, selected_normativi, selected_kolichestvo_mest):
    df=foo(selected_prohodnoi_bal, selected_normativi, selected_kolichestvo_mest)
    data0= df.loc[df['year'] == '2020']
    data1 = df.loc[df['year'] == '2021']
    data2 = df.loc[df['year'] == '2022']
    data3 = df.loc[df['year'] == '2023']
    data4 = df.loc[df['year'] == '2024']
    data5 = df.loc[df['year'] == '2025']
    fig=go.Figure(data=[
        go.Bar(name='скрыть момент времени 1', x=data0['index'], y=data0['value'], hovertext=data0['fs']),
        go.Bar(name='скрыть момент времени 2', x=data1['index'], y=data1['value'], hovertext=data1['fs']),
        go.Bar(name='скрыть момент времени 3', x=data2['index'], y=data2['value'], hovertext=data2['fs']),
        go.Bar(name='скрыть момент времени 4', x=data3['index'], y=data3['value'], hovertext=data3['fs']),
        go.Bar(name='скрыть момент времени 5', x=data4['index'], y=data4['value'], hovertext=data4['fs']),
        go.Bar(name='скрыть момент времени 6', x=data5['index'], y=data5['value'], hovertext=data5['fs'])
    ])
    fig.update_layout(barmode='group', title='Title',legend_title_text='Год')
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    ))
    return (fig)

@app.callback(
    Output('fig2', 'figure'),
    [Input('fig1', 'clickData'),
     Input('prohodnoi_bal', 'value'),
     Input('normativi', 'value'),
     Input('kolichestvo_mest', 'value')])
def display_click_data(clickData,selected_prohodnoi_bal, selected_normativi, selected_kolichestvo_mest):
    df = foo(selected_prohodnoi_bal, selected_normativi, selected_kolichestvo_mest)
    click_list=[]
    x_v=0
    for item in clickData['points']:
        click_list.append(item)
    for line in click_list:
        x_v=line["x"]
    data=df.loc[df['index'] == x_v]
    fig2 = px.bar(data_frame=data, x='index', y='value',custom_data=[data['fs']],barmode='group', hover_name='fs',color='year')

    return fig2

if __name__ == '__main__':
        app.run_server(debug=True)












