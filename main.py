from dash import Dash, html, Input, Output, State, dcc
import dash_bootstrap_components as dbc
import distanceAPIGraphHopper

app = Dash(
    external_stylesheets=["/assets/style.css", dbc.themes.BOOTSTRAP],
    title="E-Mission Possible",
)
app._favicon = "logo.jpg"

app.layout = html.Div([

    # Header
    dbc.Navbar(
        dbc.Container(
            [
                html.Div(
                    [
                        html.Img(
                            src="/assets/logo.jpg",  # Korrekte URL für Dash
                            height="50px",
                        ),
                        html.H1("E-Mission Possible", className="ms-3 text-light"),
                    ],
                    className="d-flex align-items-center",
                ),

                dbc.NavbarSimple(
                    children=[
                        dbc.NavItem(dbc.NavLink("Home", href="#")),
                        dbc.NavItem(dbc.NavLink("Log In", href="#")),
                        dbc.NavItem(dbc.NavLink("About", href="#")),
                        dbc.NavItem(dbc.NavLink("Contact", href="#")),
                    ],
                    color="success",
                    dark=True,
                ),
            ]
        ),
        color="success",
        dark=True,
    ),

    # Carousel
    dbc.Carousel(
        items=[
            {"key": "1", "src": "/assets/Bild1.jpg", "imgClassName": "img-fluid"},
            {"key": "2", "src": "/assets/Bild2.jpg", "imgClassName": "img-fluid"},
            {"key": "3", "src": "/assets/Bild3.jpg", "imgClassName": "img-fluid"},
        ],
        controls=True,
        indicators=True,
        interval=2000,
        ride="carousel"
        ),

    dbc.Container([
        # Title
        dbc.Row(
            dbc.Col(
                html.Div([
                    html.H1("E-Mission Possible", className="display-3 text-center text-primary mb-2 fw-bold"),
                    html.H3("Distance and Travel Time Calculator", className="lead text-center text-muted mb-3"),
                    html.Img(src="/assets/logo.jpg", height="100px", className="d-block mx-auto mt-3"),
                    html.H6("To enjoy the full dashboard experience, please log in.", className="display-8 lead text-center text-muted mb-3 mt-3"),
                ]),
                width=12,
            ),
            className="my-4",
            justify="center",
        ),

        # Input fields
        dbc.Row([
            dbc.Col(dbc.Input(id="input-start", placeholder="Enter start location...", type="text"), width=5),
            dbc.Col(dbc.Input(id="input-destination", placeholder="Enter destination...", type="text"), width=5),
            dbc.Col(dbc.Button("Calculate", id="btn-calculate", color="primary"), width=2),
        ], className="mb-3"),

        # Result
        dcc.Loading(
            id="loading-1",
            type="dot",
            children=[dbc.Alert("Hello Bootstrap!", color="primary", id="alert-calculation")]
        ),
    ], fluid=True)
])

# Callback function for calculating the distance and time
@app.callback(
    [Output("alert-calculation", "children"),
     Output("alert-calculation", "color")],
    Input("btn-calculate", "n_clicks"),
    State("input-start", "value"),
    State("input-destination", "value"),
)
def calculate_distance_time(n_clicks, start, destination):
    if not start or not destination:
        return "Please insert start location and destination.", "warning"
    return distanceAPIGraphHopper.get_distance_and_duration(start, destination)

if __name__ == "__main__":
    app.run_server(debug=True, port=8080)
