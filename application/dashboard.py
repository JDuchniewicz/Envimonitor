import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly.express as px
import pandas as pd

from . import query_api

def create_dashboard(server):
    """Create a Plotly Dash dashboard."""
    dash_app = dash.Dash(server=server,
                         routes_pathname_prefix='/dashapp/',
                         external_stylesheets=['/static/css/styles.css', 'https://codepen.io/chriddyp/pen/bWLwgP.css']
                         )
    # temporarily create dataframe
    df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')

    fig = px.scatter(df, x="gdp per capita", y="life expectancy",
                 size="population", color="continent", hover_name="country",
                 log_x=True, size_max=60)

    # create Dash layout
    dash_app.layout = html.Div([
        dcc.Graph(id='life-exp-vs-gdp',
            figure=fig
            ),
        dcc.Interval(
            id='interval-component',
            interval=1*1000, # TODO: change duration
            n_intervals=0
            )
        ])

    # Callbacks have to be initialized here, when Dash app is created
    init_calbacks(dash_app)

    return dash_app.server

# graph updating  in callbacks
def init_calbacks(dash_app):
    @dash_app.callback(Output('redraw-something', 'children'),
                       Input('interval-component', 'n_intervals'))
    def redraw(what):
        pass

