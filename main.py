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
    
    # Navbar
    dbc.Navbar(
        dbc.Container([

            dbc.NavbarBrand("🌱 E-Mission Possible", href="/", className="fw-bold text-white"),

            dbc.Nav([
                dbc.NavItem(dbc.NavLink("Calculator", href="/", className="text-white")),
                dbc.NavItem(dbc.NavLink("Educational Resources", href="/resources", className="text-white")),
                dbc.NavItem(dbc.NavLink("About", href="/about", className="text-white")),
                dbc.NavItem(dbc.NavLink("Contact", href="/contact", className="text-white")),
                dbc.NavItem(dbc.Button("Log In", href="/login", color="light", outline=True, className="ms-3")),
                dbc.NavItem(dbc.Button("Register", href="/register", color="light", outline=True, className="ms-3")),
            ], className="ms-auto", navbar=True),

        ], fluid=True),

        style={
            "background": "linear-gradient(90deg, #2e7d32, #66bb6a)",
            "boxShadow": "0 3px 8px rgba(0, 0, 0, 0.2)",
        },
        dark=True,
        sticky="top",
    ),

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
            dbc.Container([
                dbc.Row([
                    dbc.Col([
                        dbc.Card([
                            dbc.CardBody([
                                html.Div([

                                    # Optional: Icon
                                    html.Img(
                                        src="assets/save-the-planet.png",
                                        height="90px",
                                        className="d-block mx-auto mb-3"
                                    ),

                                    html.H2("Saving the World? There is a Login for that",
                                            className="text-center fw-bold mb-4 text-success display-4"),

                                    dbc.Input(
                                        placeholder="Enter username...",
                                        type="text",
                                        className="mb-4 form-control-lg"
                                    ),
                                    dbc.Input(
                                        placeholder="Enter password...",
                                        type="password",
                                        className="mb-4 form-control-lg"
                                    ),

                                    dbc.Button(
                                        "Log In",
                                        color="success",
                                        size="lg",
                                        className="w-100 fw-bold"
                                    ),
                                ])
                            ])
                        ], className="shadow-lg rounded-4 p-5 bg-white")
                    ], width=10, lg=8, xl=7)  # ✅ Jetzt deutlich breiter!
                ], justify="center", className="mt-5")
            ], className="vh-100 d-flex align-items-center justify-content-center")
        ])



    if pathname == "/register":
        return html.Div([
            dbc.Container([
                dbc.Row([
                    dbc.Col([
                        dbc.Card([
                            dbc.CardBody([
                                html.Div([

                                    html.H2("Join the E-Mission to a Cleaner Future 🌍",
                                            className="text-center fw-bold mb-4 text-success display-5"),

                                    dbc.Input(
                                        placeholder="Enter username...",
                                        type="text",
                                        className="mb-4 form-control-lg"
                                    ),
                                    dbc.Input(
                                        placeholder="Enter password...",
                                        type="password",
                                        className="mb-4 form-control-lg"
                                    ),

                                    dbc.Button(
                                        "Register",
                                        color="success",
                                        size="lg",
                                        className="w-100 fw-bold"
                                    ),
                                ])
                            ])
                        ], className="shadow-lg rounded-4 p-5 bg-white")
                    ], width=10, lg=8, xl=7)  # ✅ Jetzt deutlich breiter!
                ], justify="center", className="mt-5")
            ], className="vh-100 d-flex align-items-center justify-content-center")
        ])
    
    elif pathname == "/about":
        return html.Div([html.H2("About Us", className="text-center"), html.P("This is the about page.")])

    elif pathname == "/contact":
        return html.Div([html.H2("Contact Us", className="text-center"), html.P("You can reach us at contact@example.com.")])

    elif pathname == "/resources":
        return html.Div([
            html.H2("📘 Educational Resources", className="text-center my-5 fw-bold text-primary"),

            dbc.Container([

                # Section 1 – Understanding the Problem
                dbc.Row([
                    dbc.Col([
                        html.Img(src="/assets/Bild2.jpg",
                                 className="img-fluid rounded shadow-sm mb-3",
                                 style={"maxHeight": "250px", "width": "100%"}),
                        html.H4("🌍 The Impact of Transportation", className="fw-semibold text-success"),
                        html.P("Transportation is a major contributor to CO₂ emissions, air pollution, and noise. "
                               "Learn how small changes in our travel habits can create a big difference."),
                    ], width=6),

                    dbc.Col([
                        html.Img(src="/assets/Bild3.jpg",
                                 className="img-fluid rounded shadow-sm mb-3",
                                 style={"maxHeight": "250px", "width": "100%"}),
                        html.H4("♻️ Why Sustainable Mobility Matters", className="fw-semibold text-info"),
                        html.P("Public transport, cycling, and walking not only reduce emissions, but also improve health "
                               "and city life. Explore how eco-friendly travel can shape a greener future."),
                    ], width=6),
                ], className="mb-5"),

                # Section 2 – Interactive Tools
                dbc.Row([
                    dbc.Col([
                        html.H4("🧪 Interactive Learning Tools", className="fw-semibold text-primary mb-3"),
                        html.P("Explore these tools to better understand climate and transport issues:"),
                        html.Ul([
                            html.Li(html.A("🌡️ Carbon Footprint Calculator", href="https://www.carbonfootprint.com/calculator.aspx", target="_blank")),
                            html.Li(html.A("🚀 NASA Climate Kids", href="https://climatekids.nasa.gov", target="_blank")),
                            html.Li(html.A("🗺️ Sustainable Journey Game", href="https://www.cooltheearth.org", target="_blank")),
                            html.Li(html.A("📈 Emission Dashboard – Our World in Data", href="https://ourworldindata.org/co2-emissions", target="_blank")),
                        ])
                    ])
                ], className="mb-5"),

                # Section 3 – Further Reading
                dbc.Row([
                    dbc.Col([
                        html.H4("📚 Dive Deeper: Further Reading", className="fw-semibold text-warning mb-3"),
                        html.P("Trusted sources to expand your knowledge:"),
                        html.Ul([
                            html.Li(html.A("EPA – Transportation & Air Pollution", href="https://www.epa.gov/transportation-air-pollution-and-climate-change", target="_blank")),
                            html.Li(html.A("United Nations – Sustainable Transport", href="https://www.un.org/en/climatechange/transport", target="_blank")),
                            html.Li(html.A("IPCC Reports on Global Climate", href="https://www.ipcc.ch/reports/", target="_blank")),
                        ])
                    ])
                ])

            ], fluid=True, className="px-4")
        ])


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
                interval=5000,
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
