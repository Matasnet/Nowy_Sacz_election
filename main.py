import dash
from dash import dcc
from dash import html
import plotly.graph_objects as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)  # inicjacja aplikacji



app.layout = html.Div(children=[

    html.H2(children="Wybory na prezydenta miasta Nowego Sącza w latach 2018 - 2006"),
    html.Br(),
    html.P('Pod uwagę brałem tylko wyniki 2 największych kandydatów.'),


    html.H3('Wyniki z wyborów z 1 tury'),
    html.P('W roku 2010 Ryszard Nowak wygrał wybory w 1 turze. Wynik drugiego kandydata został przedstawiony w celu '
           'pokazania przewagi jaką Nowak posiadał.'),
    dcc.Graph(figure=go.Figure([
            go.Bar(
                x=['2018'],
                y=[10373],
                name='Mularczyk'
            ),
        go.Bar(
            x=['2018', '2014'],
            y=[9435, 10287],
            name='Handzel'
        ),
        go.Bar(
            x=['2014','2010', '2006'],
            y=[12335, 19789, 10129],
            name='Nowak'
        ),
        go.Bar(
            x=['2010', '2006'],
            y=[8176, 8409],
            name='Lachowicz'
        ),

        ])
    ),
    html.H3('Wyniki z wyborów z 2 tury'),
    html.P('W roku 2010 nie było drugiej tury, wtedy Ryszard Nowak wygrał w 1 turze'),
    dcc.Graph(
        figure=go.Figure([
            go.Bar(
                x=['2018'],
                y=[15046],
                name='Mularczyk'
            ),
            go.Bar(
                x=['2018', '2014'],
                y=[21078, 15197 ],
                name='Handzel'
            ),
            go.Bar(
                x=['2014', '2006'],
                y=[15385, 12670],
                name='Nowak'
            ),
            go.Bar(
                x=['2006'],
                y=[12623],
                name='Lachowicz'
            ),
        ]),
    ),

    html.Footer([html.P('Created by:'),
        html.A('Matasnet', href='https://matasdata.blogspot.com')
                        ]),
])



if __name__ == '__main__':
    app.run(debug=True)