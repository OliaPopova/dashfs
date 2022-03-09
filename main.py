import dash
import plotly.graph_objects as go
from foo import foo
from dash import dcc
from dash import html
from dash.dependencies import Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP],
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}]
                )
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.Row([
                    dbc.Card([
                        html.P(
                            "Проходной балл ЕГЭ",
                            className="card-text", style={'margin': 'auto'}),
                        dbc.CardBody([
                            dcc.Slider(id='prohodnoi_bal', value=0.75, min=0.75, max=1, step=0.01, marks=None)]),
                    ], style={"width": "25%", 'border-radius': '15px', 'margin': '-7px auto 1px', "height": "70%"}),
                    dbc.Card([
                        html.P(
                            "Нормативы",
                            className="card-text", style={'margin': 'auto'}),
                        dbc.CardBody([
                            dcc.Slider(id='normativi', value=0.7, min=0.5, max=1, step=0.01, marks=None)]),
                    ], style={"width": "25%", 'border-radius': '15px', 'margin': '-7px auto 1px', "height": "70%"}),
                    dbc.Card([
                        html.P(
                            "Количество бюджетных мест",
                            className="card-text", style={'margin': 'auto'}),
                        dbc.CardBody([
                            dcc.Slider(id='kolichestvo_mest', value=0.7, min=0.5, max=1, step=0.01, marks=None)]),
                    ], style={"width": "25%", 'border-radius': '15px', 'margin': '-7px auto 1px', "height": "70%"}),
                ], align="center"),
            ], style={'backgroundColor': '#686c6e', 'font-weight': 'semibold', 'font': 'Open Sans',
                      'border-radius': '10px', 'margin': '2% auto 0%', "height": "75%"}),
        ], width={'size': 10, 'offset': 1}),
    ], style={'background-color': '#323436'}),
    dbc.Row([
        dbc.Col(
            html.Div(
                dcc.Graph(id='fig1', figure={}, config={
                    'staticPlot': False,  # True, False
                    'displayModeBar': False,  # True, False, 'hover'
                    'watermark': True,
                }))
        )

    ], style={'background-color': '#323436'}),  # Horizontal:start,center,end,between,around

    dbc.Row([
        dbc.Col(
            html.Div(id="graph-container",
                     children=[
                         dcc.Graph(id='fig2', figure={}, config={
                             'staticPlot': False,  # True, False
                             'displayModeBar': False,  # True, False, 'hover'
                             'watermark': True
                         })]),
        ),

    ], style={'background-color': '#323436'}),

    dbc.Row([
        dbc.Col(
            dbc.Card([
                html.P(
                    "Количество обучающихся в классе профильного обучения.",
                    className="card-text", style={'margin-left': '3%'}),
                html.P(
                    "Информация о факторе.",
                    className="card-text", style={'margin-left': '3%'}),
                html.P(
                    " Какие показатели влияют на данный фактор.",
                    className="card-text", style={'margin-left': '3%'})
            ], style={"width": "40%", 'font-weight': 'semibold', 'font': 'Open Sans', 'border-radius': '15px',
                      'margin': '2% 3% 2% 2%'})
        ),
    ], style={'background-color': '#323436'})
], fluid=True)


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
        go.Bar(name='скрыть 2020 г.', x=data0['index'], y=data0['value'], hovertext=data0['fs'],
               marker_color='#2dbfcf'),
        go.Bar(name='скрыть 2021 г.', x=data1['index'], y=data1['value'], hovertext=data1['fs'],
               marker_color='#309190'),
        go.Bar(name='скрыть 2022 г.', x=data2['index'], y=data2['value'], hovertext=data2['fs'],
               marker_color='#387bc7'),
        go.Bar(name='скрыть 2023 г.', x=data3['index'], y=data3['value'], hovertext=data3['fs'],
               marker_color='#465c66'),
        go.Bar(name='скрыть 2024 г.', x=data4['index'], y=data4['value'], hovertext=data4['fs'],
               marker_color='#558787'),
        go.Bar(name='скрыть 2025 г.', x=data5['index'], y=data5['value'], hovertext=data5['fs'],
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
    if clickData:
        df = foo(selected_prohodnoi_bal, selected_normativi, selected_kolichestvo_mest)
        x_v = 0
        for line in clickData['points']:
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
            yaxis_title=None, title_x=0.5)
        fig2.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
        fig2.update_layout(legend=None)
        for data in fig2.data:
            data["width"] = 0.35
        return fig2
    else:
        fig_empty=px.bar()
        return fig_empty



@app.callback(Output('graph-container', 'style'), [Input('fig1', 'clickData')])
def hide_graph(clickData):
    if clickData:
        return {'display':'block'}
    return {'display':'none'}

if __name__ == '__main__':
    app.run_server(debug=True, port=8000)
