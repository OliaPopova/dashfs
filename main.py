import plotly.express as px
import dash
import dash_daq as daq
import plotly.express as px
import plotly.graph_objects as go
from dash import dcc, html, Input, Output
from foo import foo
import dash_bootstrap_components as dbc

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

app.layout = html.Div(children=[
    html.Div([
        dbc.Card([
            dbc.Card([
                dbc.CardHeader("Проходной балл ЕГЭ"),
                dbc.CardBody([
                    daq.Slider(id='prohodnoi_bal', value=0.75, min=0.75, max=1, step=0.01, marks=None,
                               size=200)], style={'margin-right':'7%','margin-left':'7%'}),
            ],
                style={"width": "35%", 'backgroundColor': 'white', 'display': 'inline-block',
                       'border-radius': '10px', 'margin-left': '7%', 'margin-top':'0.5%', 'margin-bottom':'0.5%', 'text-align': 'center'}),
            dbc.Card([
                dbc.CardHeader("Нормативы"),
                dbc.CardBody([
                    daq.Slider(id='normativi', value=0.7, min=0.5, max=1, step=0.01,
                               marks={'25': 'mark', '50': '50'},
                               size=200)], style={'margin-right':'7%','margin-left':'7%'}),
            ],
                style={"width": "35%", 'backgroundColor': 'white', 'display': 'inline-block',
                       'border-radius': '10px', 'margin-left': '7%','margin-top':'0.5%','margin-bottom':'0.5%','text-align': 'center'}),
            dbc.Card([
                dbc.CardHeader("Количество бюджетных мест"),
                dbc.CardBody([
                    daq.Slider(id='kolichestvo_mest', value=0.7, min=0.5, max=1, step=0.01,
                               marks={'25': 'mark', '50': '50'},
                               size=200)], style={'margin-right':'7%','margin-left':'7%',}),
            ], style={"width":'35%', 'backgroundColor': 'white', 'display': 'inline-block',
                      'border-radius': '10px','margin-left': '7%','margin-right': '7%','margin-top':'0.5%', 'margin-bottom':'0.5%', 'text-align': 'center'}),
        ],  style={'backgroundColor': '#686c6e', 'border-radius': '10px', 'display': 'flex',
                    'justify-content': 'space-between', "width":'70%','height': '5.5rem', 'margin-top':'3%', 'margin-right': '15%', 'margin-left': '15%'}),
        html.Div(
            dcc.Graph(id='fig1',
                      style={'backgroundColor': 'gray', 'border-radius': '10px'}), className="card"),
        html.Div(
            dcc.Graph(id='fig2',
                      style={'backgroundColor': 'gray', 'border-radius': '10px'}), className="card"),

        dbc.Card([
            html.Div(children='''
                Количество обучающихся в классе профильного обучения.
            '''),
            html.Div(children='''
                Информация о факторе.
            '''),
            html.Div(children='''
                Какие показатели влияют на данный фактор.
            '''),
        ], style={'width': '33%', 'backgroundColor': 'white', 'border-radius': '10px','margin-left': '3%','margin-top':'3%'})
    ], style={'background-color': '#323436'}
    )
], style={'background-color': '#323436'})


@app.callback(
    Output('fig1', 'figure'),
    [Input('prohodnoi_bal', 'value'),
     Input('normativi', 'value'),
     Input('kolichestvo_mest', 'value')])
# create our callback function
def update_figure(selected_prohodnoi_bal, selected_normativi, selected_kolichestvo_mest):
    df = foo(selected_prohodnoi_bal, selected_normativi, selected_kolichestvo_mest)
    data0 = df.loc[df['year'] == '2020']
    data1 = df.loc[df['year'] == '2021']
    data2 = df.loc[df['year'] == '2022']
    data3 = df.loc[df['year'] == '2023']
    data4 = df.loc[df['year'] == '2024']
    data5 = df.loc[df['year'] == '2025']
    fig = go.Figure(data=[
        go.Bar(name='скрыть момент времени 1', x=data0['index'], y=data0['value'], hovertext=data0['fs'],
               marker_color='#2dbfcf'),
        go.Bar(name='скрыть момент времени 2', x=data1['index'], y=data1['value'], hovertext=data1['fs'],
               marker_color='#309190'),
        go.Bar(name='скрыть момент времени 3', x=data2['index'], y=data2['value'], hovertext=data2['fs'],
               marker_color='#387bc7'),
        go.Bar(name='скрыть момент времени 4', x=data3['index'], y=data3['value'], hovertext=data3['fs'],
               marker_color='#465c66'),
        go.Bar(name='скрыть момент времени 5', x=data4['index'], y=data4['value'], hovertext=data4['fs'],
               marker_color='#558787'),
        go.Bar(name='скрыть момент времени 6', x=data5['index'], y=data5['value'], hovertext=data5['fs'],
               marker_color='#b6d3e0')
    ])
    fig.update_layout(barmode='group', legend_title_text='Год', yaxis_range=[0, 30],
                      plot_bgcolor='#565859',
                      paper_bgcolor='#323436', font_color="#bec4c4")
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
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
def display_click_data(clickData, selected_prohodnoi_bal, selected_normativi, selected_kolichestvo_mest):
    df = foo(selected_prohodnoi_bal, selected_normativi, selected_kolichestvo_mest)
    click_list = []
    x_v = 0
    for item in clickData['points']:
        click_list.append(item)
    for line in click_list:
        x_v = line["x"]
    data = df.loc[df['index'] == x_v]
    for fs in data['fs']:
        title = fs
    fig2 = px.bar(data_frame=data, x='year', y='value', custom_data=[data['fs']], hover_name='fs',
                  color='year',
                  color_discrete_map={
                      '2020': '#2dbfcf',
                      '2021': '#309190',
                      '2022': '#387bc7',
                      '2023': '#465c66',
                      '2024': '#35b0e6',
                      '2025': '#b6d3e0'}, template='plotly', title=title)
    fig2.update_layout(
                       plot_bgcolor='#565859',
                       paper_bgcolor='#323436', font_color="#bec4c4", xaxis_title=None,
                       yaxis_title=None)
    fig2.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
    return fig2


if __name__ == '__main__':
    app.run_server(debug=True)
