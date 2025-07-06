from dash import Dash, html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
import distanceAPIGraphHopper
import ssl
import certifi
import geopy.geocoders
from dash import dcc
import plotly.graph_objs as go

geopy.geocoders.options.default_ssl_context = ssl.create_default_context(cafile=certifi.where())

app = Dash(
    external_stylesheets=["/assets/style.css", dbc.themes.BOOTSTRAP],
    title="E-Mission Possible",
    suppress_callback_exceptions=True,
)
app._favicon = "logo.jpg"

app.layout = html.Div([
dcc.Location(id="url", refresh=False),

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

                                    html.Img(
                                        src="assets/save-the-planet.png",
                                        height="90px",
                                        className="d-block mx-auto mb-3"
                                    ),

                                    html.H2("Saving the World? There's a Login for that",
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
                                        "Log In",
                                        color="success",
                                        size="lg",
                                        className="w-100 fw-bold"
                                    ),
                                ])
                            ])
                        ], className="shadow-lg rounded-4 p-5 bg-white")
                    ], width=10, lg=8, xl=7)
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
                    ], width=10, lg=8, xl=7)
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


    else:  # Homepage / Calculator Page
        return html.Div([
            dbc.Carousel(
                items=[
                    {"key": "1", "src": "/assets/Bild1.jpg", "imgClassName": "img-fluid"},
                    {"key": "2", "src": "/assets/Bild2.jpg", "imgClassName": "img-fluid"},
                    {"key": "3", "src": "/assets/Bild3.jpg", "imgClassName": "img-fluid"},
                ],
                controls=True,
                indicators=True,
                interval=3000,
                ride="carousel",
                className="carousel mb-5"
            ),

            dbc.Container([
                dbc.Row([
                    dbc.Col([
                        html.Div([
                            html.H1("E-Mission Possible", className="display-3 fw-bold text-success text-center"),
                            html.H4("Plan Smarter. Travel Greener.", className="text-muted text-center mb-4"),
                        ])
                    ], width=12)
                ], justify="center"),

                dbc.Row([
                    dbc.Col(dbc.Input(
                        id="input-start",
                        placeholder="🌍 Start location...",
                        type="text",
                        className="form-control-lg"
                    ), width=4),

                    dbc.Col(dbc.Input(
                        id="input-destination",
                        placeholder="🚩 Destination...",
                        type="text",
                        className="form-control-lg"
                    ), width=4),

                    dbc.Col(
                        dcc.Dropdown(
                            id="input-vehicle",
                            options=[
                                {"label": "Car", "value": "car"},
                                {"label": "Bike", "value": "bike"},
                                {"label": "Walk", "value": "foot"},
                            ],
                            value="car",
                            clearable=False,
                            style={"width": "100%", "height": "40px", "fontSize": "1.1rem"}
                        ),
                        width=2,
                        className="d-flex align-items-center"
                    ),

                    dbc.Col(dbc.Button(
                        "Calculate",
                        id="btn-calculate",
                        color="success",
                        size="lg",
                        className="w-100"
                    ), width=2),
                ], className="mb-4"),

                dbc.Row([
                    dbc.Col([
                        dcc.Loading(
                            id="loading-1",
                            type="circle",
                            color="#198754",  # Bootstrap green
                            children=[
                                dbc.Alert("Please enter a route to get started.",
                                          color="light",
                                          id="alert-calculation",
                                          className="text-center fw-semibold shadow-sm")
                            ]
                        )
                    ], width=12)
                ])
            ], fluid=True, className="py-5")
        ])

# Callback function for calculating the distance and time via API
@app.callback(
    [Output("alert-calculation", "children"),
     Output("alert-calculation", "color")],
    Input("btn-calculate", "n_clicks"),
    State("input-start", "value"),
    State("input-destination", "value"),
    State("input-vehicle", "value"),
)
def calculate_distance_time(n_clicks, start, destination, vehicle):
    if not start or not destination:
        return "Please insert start location and destination.", "warning"

    distance_km, duration_min, status = distanceAPIGraphHopper.get_distance_and_duration(start, destination, vehicle)
    if status != "success":
        return f"Error: {status}", "danger"

    stats_card = eco_stats_card(distance_km, duration_min, vehicle)
    co2_graph = co2_emissions_graph(distance_km)

    return html.Div([stats_card, co2_graph]), "success"

# Stats

def eco_stats_card(distance_km, duration_min, vehicle):
    co2_per_km_map = {
        "car": 120,
        "bike": 0,
        "foot": 0,
    }
    co2_per_km = co2_per_km_map.get(vehicle)
    co2_saved = distance_km * co2_per_km  # you can improve this logic for savings compared to car

    calories_burned = distance_km * (50 if vehicle in ["bike", "foot"] else 0)
    trees_needed = co2_saved / 21000

    return dbc.Card([
        dbc.CardBody([
            html.H4("Your Eco Impact", className="card-title text-success mb-3"),
            html.P(f"Distance: {distance_km:.2f} km"),
            html.P(f"Estimated Time: {duration_min:.0f} min"),
            html.P(f"CO₂ Emissions: {co2_saved/1000:.2f} kg 🌿"),
            html.P(f"Calories Burned: {calories_burned:.0f} kcal 🚴" if calories_burned > 0 else ""),
            html.P(f"Equivalent to offset by {trees_needed:.1f} trees 🌳"),
        ])
    ], className="shadow-sm bg-light border-success mt-4")

# Graphs

def co2_emissions_graph(distance_km):
    co2_car = distance_km * 120  # grams CO2
    co2_bike = 0
    co2_public_transport = distance_km * 60  # example number

    data = [
        go.Bar(name='Car', x=['CO₂ Emissions'], y=[co2_car]),
        go.Bar(name='Bike/Walk', x=['CO₂ Emissions'], y=[co2_bike]),
        go.Bar(name='Public Transport', x=['CO₂ Emissions'], y=[co2_public_transport]),
    ]

    layout = go.Layout(
        title="CO₂ Emissions Comparison (grams)",
        yaxis=dict(title="Grams CO₂"),
        barmode='group',
        plot_bgcolor='rgba(0,0,0,0)',  # transparent background
        paper_bgcolor='rgba(0,0,0,0)'
    )

    fig = go.Figure(data=data, layout=layout)
    return dcc.Graph(figure=fig)


if __name__ == "__main__":
    app.run_server(debug=True, port=8080)
