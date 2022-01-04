import dash
from dash.html.Tr import Tr
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

# init dash app
app = dash.Dash(__name__)

# define test df
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

df2 = pd.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')

colors = {
    'background':'#111111',
    'text':'#7FDBFF'
}


fig = px.bar(df, x ='Fruit', y ='Amount', color='City', barmode='group')

fig2 = px.scatter(df2, x="gdp per capita", y="life expectancy",
                 size="population", color="continent", hover_name="country",
                 log_x=True, size_max=60)

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

fig2.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

app.layout = html.Div(
    [
    html.Div(
        style={'backgroundColor': colors['background']}, 
        children=[
        html.H1(
            children='Hello Dash!', 
            style= {
                'textAlign':'center',
                'color':colors['text'],
                }
            ),
        html.Div(
            children='A web application framework for your data ',
            style={
                'textAlign':'center',
                'color':colors['text']
                },        
            ),
        dcc.Graph(
            id='example-graph',
            figure=fig
            ),
        dcc.Graph(
            id='example-graph3',
            figure=fig
            ),

        ]),
    html.Div(
        style={'backgroundColor': colors['background']}, 
        children=[
        html.H1(
            children='Hello Dash!', 
            style= {
                'textAlign':'center',
                'color':colors['text'],
                }
            ),
        html.Div(
            children='A web application framework for your data ',
            style={
                'textAlign':'center',
                'color':colors['text']
                },        
            ),
        dcc.Graph(
            id='example-graph2 ',
            figure=fig2
            )
        ]),
        
], style=({'width': '70%', 'display': 'inline-block', 'vertical-align': 'right'}))



if __name__ == '__main__':
    app.run_server(debug=True)

