from dash import Dash, html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
import distanceAPIGraphHopper
import ssl
import certifi
import geopy.geocoders

geopy.geocoders.options.default_ssl_context = ssl.create_default_context(cafile=certifi.where())

app = Dash(
    external_stylesheets=["/assets/style.css", dbc.themes.BOOTSTRAP],
    title="E-Mission Possible",
    suppress_callback_exceptions=True,
)
app._favicon = "logo.jpg"

app.layout = html.Div([
dcc.Location(id="url", refresh=False),  # 🔹 URL-Tracking-Element
    
    # Navbar bleibt immer sichtbar
    dbc.Navbar(
        dbc.Container([
            dbc.NavbarSimple(
                children=[
                    dbc.NavItem(dbc.NavLink("Home", href="/")),
                    dbc.NavItem(dbc.NavLink("Log In", href="/login")),
                    dbc.NavItem(dbc.NavLink("About", href="/about")),
                    dbc.NavItem(dbc.NavLink("Contact", href="/contact")),
                ],
                className="ms-auto",
                color="transparent",
                dark=True,
            ),
        ], fluid=True),
        color="transparent",
        dark=True,
    ),
    
    # Hier wird die Seite dynamisch aktualisiert
    html.Div(id="page-content")
])

# 🔹 Callback für Seitenwechsel
@app.callback(
    Output("page-content", "children"),
    Input("url", "pathname")
)
def display_page(pathname):
    if pathname == "/login":
        return html.Div([
            html.H2("Login Page", className="h2"),
            dbc.Container([
                dbc.Row(dbc.Col(dbc.Input(placeholder="Enter username...", className="logInFelder", type="text"), width=6), justify="center"),
                dbc.Row(dbc.Col(dbc.Input(placeholder="Enter password...", type="password"), width=6), justify="center"),
                dbc.Row(dbc.Col(dbc.Button("Log In", color="primary"), width=6, className="buttonLogIn"), justify="center"),
            ], className="mt-4")
        ])
    
    elif pathname == "/about":
        return html.Div([html.H2("About Us", className="text-center"), html.P("This is the about page.")])

    elif pathname == "/contact":
        return html.Div([html.H2("Contact Us", className="text-center"), html.P("You can reach us at contact@example.com.")])
    
    else:  # Standard-Homepage (z.B. Startseite)
        return html.Div([
            dbc.Carousel(
                items=[
                    {"key": "1", "src": "/assets/Bild1.jpg", "imgClassName": "img-fluid"},
                    {"key": "2", "src": "/assets/Bild2.jpg", "imgClassName": "img-fluid"},
                    {"key": "3", "src": "/assets/Bild3.jpg", "imgClassName": "img-fluid"},
                ],
                controls=True,
                indicators=True,
                interval=2000,
                ride="carousel",
                className="carousel"
            ),
            dbc.Container([
                dbc.Row(
                    dbc.Col(
                        html.Div([
                            html.H1("E-Mission Possible", className="display-3 text-center fw-bold"),
                            html.H3("Distance and Travel Time Calculator", className="lead text-center text-muted"),
                            html.H6("To enjoy the full dashboard experience, please log in.", className="display-8 lead text-center text-muted"),
                        ]),
                        width=12,
                    ),
                    className="my-4",
                    justify="center",
                ),
                dbc.Row([
                    dbc.Col(dbc.Input(id="input-start", placeholder="Enter start location...", type="text"), width=5),
                    dbc.Col(dbc.Input(id="input-destination", placeholder="Enter destination...", type="text"), width=5),
                    dbc.Col(dbc.Button("Calculate", id="btn-calculate", color="primary"), width=2),
                ], className="mb-3"),
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
