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
                    dbc.NavItem(dbc.NavLink("Calculator", href="/")),
                    dbc.NavItem(dbc.NavLink("Educational Resources", href="/resources")),
                    dbc.NavItem(dbc.NavLink("About", href="/about")),
                    dbc.NavItem(dbc.NavLink("Contact", href="/contact")),
                ],
                className="ms-auto",
                color="transparent",
                dark=True,
            ),
            dbc.NavItem(
                dbc.Button("Log In", href="/login", id="btn-login", color="primary", outline=False, className="ms-2 fw-semibold shadow-sm")
            ),
            dbc.NavItem(
                dbc.Button("Register", href="/register", id="btn-register", color="primary", outline=False, className="ms-2 fw-semibold shadow-sm")
            ),
        ], fluid=True),
        color="transparent",
        dark=True,
        id="navbar"
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
            html.H2("Saving the World? There's a Login for that 🌲", className="h2"),
            dbc.Container([
                dbc.Row(dbc.Col(dbc.Input(placeholder="Enter username...", className="logInFelder", type="text"), width=6), justify="center"),
                dbc.Row(dbc.Col(dbc.Input(placeholder="Enter password...", type="password"), width=6), justify="center"),
                dbc.Row(dbc.Col(dbc.Button("Log In", href="/dashboard", color="primary"), width=6, className="buttonLogIn"), justify="center"),
            ], className="mt-4")
        ])

    if pathname == "/register":
        return html.Div([
            html.H2("The Road to Sustainability Starts Here. 🌍", className="h2"),
            dbc.Container([
                dbc.Row(dbc.Col(dbc.Input(placeholder="Enter email...", className="logInFelder", type="text"), width=6), justify="center"),
                dbc.Row(dbc.Col(dbc.Input(placeholder="Enter password...", type="password"), width=6), justify="center"),
                dbc.Row(dbc.Col(dbc.Button("Register", href="/dashboard", color="primary"), width=6, className="buttonLogIn"), justify="center"),
            ], className="mt-4")
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

    elif pathname == "/dashboard":
        monthly_savings = {
            'Months': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
            'CO2 Saved (kg)': [13, 16, 21, 18, 19, 23, 
                            17, 0, 0, 0, 0, 0]  # Sum should be ~127kg
        }
        
        # Create the figure
        fig = {
            'data': [
                {
                    'x': monthly_savings['Months'],
                    'y': monthly_savings['CO2 Saved (kg)'],
                    'type': 'bar',
                    'name': 'CO₂ Savings',
                    'marker': {'color': '#28a745'}
                }
            ],
            'layout': {
                'title': 'Monthly CO₂ Savings (Total: 127 kg)',
                'xaxis': {'title': 'Month'},
                'yaxis': {'title': 'CO₂ Saved (kg)'},
                'plot_bgcolor': 'rgba(0,0,0,0)',
                'paper_bgcolor': 'rgba(0,0,0,0)',
                'font': {'color': '#008000'}
            }
        }
        return html.Div([
            # Header section
            html.Div([
                html.H2("Your Sustainability Dashboard", 
                    className="text-center mb-3",
                    style={"font-weight": "bolder", "font-size": "3em"}), 
                html.P("Track your eco-friendly progress with E-Mission Possible", 
                    className="text-center mb-4 text-success",
                    style={"font-weight": "bold"})
            ], className="container"),
            
            # Three environmental metric cards
            dbc.Container([
                dbc.Row([
                    # Card 1: CO2 Savings
                    dbc.Col(
                        dbc.Card(
                            [
                                html.Div("🌍", className="text-center display-4 mt-3"),  # Earth emoji
                                dbc.CardBody([
                                    html.H4("CO₂ Savings", className="card-title text-center", style={"color": "#008000"}),
                                    html.H2("127 kg", className="text-center my-3"),  # Demo value
                                    html.P("Equivalent to planting 6 trees", 
                                        className="card-text text-center", 
                                        style={"color": "#008000"})
                                ])
                            ],
                            className="h-100",
                            style={
                                "border-radius": "15px",
                                "box-shadow": "0 4px 8px rgba(0,0,0,0.1)",
                                "border-top": "4px solid #28a745"  # Green accent
                            }
                        ),
                        md=4, className="mb-4"
                    ),
                    
                    # Card 2: Energy Efficiency
                    dbc.Col(
                        dbc.Card(
                            [
                                html.Div("⚡", className="text-center display-4 mt-3"),  # Lightning emoji
                                dbc.CardBody([
                                    html.H4("Energy Saved", className="card-title text-center", style={"color": "#008000"}),
                                    html.H2("342 kWh", className="text-center my-3"),  # Demo value
                                    html.P("Enough to power a home for 11 days", 
                                        className="card-text text-center", 
                                        style={"color": "#008000"})
                                ])
                            ],
                            className="h-100",
                            style={
                                "border-radius": "15px",
                                "box-shadow": "0 4px 8px rgba(0,0,0,0.1)",
                                "border-top": "4px solid #ffc107"  # Yellow accent
                            }
                        ),
                        md=4, className="mb-4"
                    ),
                    
                    # Card 3: Alternative Transport
                    dbc.Col(
                        dbc.Card(
                            [
                                html.Div("🚲", className="text-center display-4 mt-3"),  # Bike emoji
                                dbc.CardBody([
                                    html.H4("Green Miles", className="card-title text-center", style={"color": "#008000"}),
                                    html.H2("89 km", className="text-center my-3"),  # Demo value
                                    html.P("Using bikes/public transport instead of cars", 
                                        className="card-text text-center", 
                                        style={"color": "#008000"})
                                ])
                            ],
                            className="h-100",
                            style={
                                "border-radius": "15px",
                                "box-shadow": "0 4px 8px rgba(0,0,0,0.1)",
                                "border-top": "4px solid #17a2b8"  # Teal accent
                            }
                        ),
                        md=4, className="mb-4"
                    )
                ], justify="center", className="g-4")
            ], fluid="md"),
            dbc.Container([
                dbc.Card([
                    dbc.CardHeader("CO₂ Savings Over Time (Year-to-Date)", className="text-success", style={"font-weight": "bold"}),
                    dbc.CardBody([
                        dcc.Graph(
                            id='co2-graph',
                            figure=fig,
                            config={'displayModeBar': False}
                        ),
                        
                    html.P("Your monthly CO₂ savings from using sustainable transportation options.",
                        className="text-muted text-center mt-2"), 
                    html.P("Remember: Your annual CO₂ emissions are on average 10.3 tons", 
                        className="text-muted text-center mt-2"), 

                    ])
                ], className="mt-4",
                style={"border-radius": "15px", "box-shadow": "0 4px 8px rgba(0,0,0,0.1)"})
            ], fluid="md", className="mb-5")
        ], className="py-4")

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
