
import plotly.express as px
import dash_daq as daq
import dash
from dash import Dash, dcc, html, Input, Output
from foo import foo


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

app.layout = html.Div( children=[
    html.H1(children="Дашборд",),

    html.Div([
                html.Div(children='''Проходной балл ЕГЭ'''),

                daq.Slider(id='prohodnoi_bal',value=0.75, min=0.75, max=1, step=0.01,marks=None, size=200),
                ], style = {'width': '70%', 'padding-left': '10%', 'padding-right': '20%'} ),

    html.Div([
                html.Div(children='''Нормативы'''),

                daq.Slider(id='normativi',value=0.51, min=0.51, max=1, step=0.01,marks=None, size=200),
                ], style = {'width': '70%', 'padding-left': '35%', 'padding-right': '20%'} ),

    html.Div([
                 html.Div(children='''Количество бюджетных мест '''),

                daq.Slider(id='kolichestvo_mest',value=0.7, min=0.5, max=1, step=0.01,  marks={'25': 'mark', '50': '50'}, size=200),
                ], style = {'width': '70%', 'padding-left': '60%', 'padding-right': '20%'} ),

    dcc.Graph(id='fig1',
              style={'background':'#1d1e1f'})
    ]
    )
@app.callback(
    Output('fig1', 'figure'),
    [Input('prohodnoi_bal', 'value'),
    Input('normativi', 'value'),
    Input('kolichestvo_mest', 'value')])

def update_figure(selected_prohodnoi_bal, selected_normativi, selected_kolichestvo_mest):
    df=foo(selected_prohodnoi_bal, selected_normativi, selected_kolichestvo_mest)

    fig = px.bar(data_frame=df, x='index', y='value', custom_data=[df['fs']],barmode='group', hover_name='fs', color='year')
    fig.update_traces()
    return fig

if __name__ == '__main__':
        app.run_server(debug=True)












