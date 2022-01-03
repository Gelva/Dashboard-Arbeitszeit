import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go
import plotly.express as px 
from dash.dependencies import Input, Output 


# init dash app
app = dash.Dash()
df = px.data.stocks()

def stock_prices():
    # Function for creating line chart showing Google stock prices over time 
    fig = go.Figure([go.Scatter(x = df['date'], y = df['GOOG'],\
                     line = dict(color = 'firebrick', width = 4), name = 'Google')
                     ])
    fig.update_layout(title = 'Prices over time',
                      xaxis_title = 'Dates',
                      yaxis_title = 'Prices'
                      )
    return fig

app.layout = html.Div(id = 'parent', children = [
    html.H1(id = 'H1', children = 'Styling using html components', style = {'textAlign':'center',\
                                            'marginTop':40,'marginBottom':40}),

        
        dcc.Graph(id = 'line_plot', figure = stock_prices())    
    ]
                     )

dcc.Dropdown( id = 'dropdown',
            options = [
                {'label':'Google', 'value':'GOOG' },
                {'label': 'Apple', 'value':'AAPL'},
                {'label': 'Amazon', 'value':'AMZN'},
                ],
            value = 'GOOGL'       
            )


                     

if __name__ == '__main__': 
    app.run_server()