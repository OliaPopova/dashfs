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
server = app.server
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.Row([
                    dbc.Card([
                        html.P(
                            "Проходной балл ЕГЭ",
                            className="card-text",
                            style={'margin': '0px 0px 0px 14%', 'font-size': '18px', 'font-weight': 'normal',
                                   'font-family': 'Open Sans'}),
                        dbc.CardBody([
                            dcc.Slider(id='prohodnoi_bal', value=0.75, min=0.75, max=1, step=0.01, marks=None,tooltip={"placement": "bottom", "always_visible": True})]),
                    ], style={"width": "25%", 'border-radius': '15px', "border":"1px #E0E0E0",  'margin': '-7px auto 1px', "height": "70%"}),
                    dbc.Card([
                        html.P(
                            "Нормативы",
                            className="card-text",
                            style={'margin': '0px 0px 0px 14%', 'font-size': '18px', 'font-weight': 'normal',
                                   'font-family': 'Open Sans'}),
                        dbc.CardBody([
                            dcc.Slider(id='normativi', value=0.6, min=0.51, max=1, step=0.01, marks=None, tooltip={"placement": "bottom", "always_visible": True})]),
                    ], style={"width": "25%", 'border-radius': '15px', "border":"1px #E0E0E0",  'margin': '-7px auto 1px', "height": "70%"}),
                    dbc.Card([
                        html.P(
                            "Количество бюджетных мест",
                            className="card-text",
                            style={'margin': '0px 0px 0px 14%', 'font-size': '18px', 'font-weight': 'normal',
                                   'font-family': 'Open Sans'}),
                        dbc.CardBody([
                            dcc.Slider(id='kolichestvo_mest', value=0.5, min=0.5, max=1, step=0.01, marks=None, tooltip={"placement": "bottom", "always_visible": True})]),
                    ], style={"width": "25%", 'border-radius': '15px', "border":"1px #E0E0E0",  'margin': '-7px auto 1px', "height": "70%"}),
                ], align="center"),
            ], style={'backgroundColor': '#686c6e', 'font-weight': 'semi-bold', 'font': 'Open Sans',
                      'border-radius': '10px', 'margin': '2% auto 0%', "height": "75%"}),
        ], width={'size': 10, 'offset': 1}),
    ], style={'background-color': '#323436', 'margin-bottom': '2% '}),
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
                         }),

                         dbc.Card([
                             html.P(
                                 "Количество обучающихся в классе профильного обучения.",
                                 className="card-text",
                                 style={'margin-left': '3%', 'font-size': '20px', 'font-weight': 'bold',
                                        'font-family': 'Open Sans'}),
                             html.P(
                                 "Информация о факторе.",
                                 className="card-text",
                                 style={'margin-left': '3%', 'font-size': '20px', 'font-weight': 'bold',
                                        'font-family': 'Open Sans'}),
                             html.P(
                                 " Какие показатели влияют на данный фактор.",
                                 className="card-text",
                                 style={'margin-left': '3%', 'font-size': '20px', 'font-weight': 'bold',
                                        'font-family': 'Open Sans'})
                         ], style={"width": "40%", 'font-weight': 'semibold', 'font': 'Open Sans',
                                   'border-radius': '15px',
                                   'margin': '2% 3% 2% 5%'})
                     ]),

        ),
    ], style={'background-color': '#323436'}),

], style={'height': '100vh', 'background-color': '#323436'}, fluid=True)


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
               marker_color='#1fad94'),
        go.Bar(name='скрыть 2022 г.', x=data2['index'], y=data2['value'], hovertext=data2['fs'],
               marker_color='#148e95'),
        go.Bar(name='скрыть 2023 г.', x=data3['index'], y=data3['value'], hovertext=data3['fs'],
               marker_color='#0068b4'),
        go.Bar(name='скрыть 2024 г.', x=data4['index'], y=data4['value'], hovertext=data4['fs'],
               marker_color='#309ec1'),
        go.Bar(name='скрыть 2025 г.', x=data5['index'], y=data5['value'], hovertext=data5['fs'],
               marker_color='#b0d9ff')
    ])
    fig.update_layout(legend_title_text='Год', yaxis_range=[0, 10],
                      plot_bgcolor='#565859',
                      paper_bgcolor='#323436', font_color="white", margin=dict(b=10, pad=15))
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.06,
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
                          '2021': '#1fad94',
                          '2022': '#148e95',
                          '2023': '#0068b4',
                          '2024': '#309ec1',
                          '2025': '#b0d9ff'}, template='plotly', title=title)
        fig2.update_layout(
            plot_bgcolor='#565859',
            paper_bgcolor='#323436', font_color="white", xaxis_title=None,
            yaxis_title=None,yaxis_range=[0, 15], title_x=0.5, margin=dict(b=10, pad=15))
        fig2.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.06,
            xanchor="right",
            x=1,
            title='Год'
        ))
        fig2.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
        for data in fig2.data:
            data["width"] = 0.35
        return fig2
    else:
        fig_empty = px.bar()
        return fig_empty


@app.callback(Output('graph-container', 'style'), [Input('fig1', 'clickData')])
def hide_graph(clickData):
    if clickData:
        return {'display': 'block'}
    return {'display': 'none'}


if __name__ == '__main__':
    app.run_server(debug=True)
