from dash import Dash, html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
import distanceAPIGraphHopper
import ssl
import certifi
import geopy.geocoders
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
        return html.Div(
            style={
                'background-image': 'url("/assets/WaldVogelperspektive.jpg")',
                'background-size': 'cover',
                'height': '100vh',
                'display': 'flex',
                'justify-content': 'center',
                'align-items': 'center',
                'padding': '20px'
            },
            children=dbc.Card(
                style={
                    'width': '400px',
                    'padding': '2rem',
                    'border-radius': '15px',
                    'box-shadow': '0 10px 20px rgba(0,0,0,0.1)',
                    'background': 'rgba(255,255,255,0.95)'
                },
                children=[
                    html.Div(
                        className="text-center mb-4",
                        children=[
                            html.Img(src="/assets/Bild4.png", style={'height': '80px'}),
                            html.H2("Welcome Back", style={'color': '#28a745', 'margin-top': '1rem'})
                        ]
                    ),
                    dbc.Input(placeholder="Email", type="email", className="mb-3"),
                    dbc.Input(placeholder="Password", type="password", className="mb-4"),
                    dbc.Button("Login",
                               color="success",
                               className="w-100 mb-3",
                               href="/dashboard"),
                    html.Div(
                        className="text-center mt-3",
                        children=[
                            html.Span("Don't have an account? "),
                            html.A("Register here", href="/register", style={'color': '#28a745'})
                        ]
                    )
                ]
            )
        )

    if pathname == "/register":
        return html.Div(
            style={
                'background-image': 'url("/assets/WaldVogelperspektive.jpg")',
                'background-size': 'cover',
                'height': '100vh',
                'display': 'flex',
                'justify-content': 'center',
                'align-items': 'center',
                'padding': '20px'
            },
            children=dbc.Card(
                style={
                    'width': '400px',
                    'padding': '2rem',
                    'border-radius': '15px',
                    'box-shadow': '0 10px 20px rgba(0,0,0,0.1)',
                    'background': 'rgba(255,255,255,0.95)'
                },
                children=[
                    html.Div(
                        className="text-center mb-4",
                        children=[
                            html.Img(src="/assets/Bild4.png", style={'height': '80px'}),
                            html.H2("Welcome to E-Mission Possible", style={'color': '#28a745', 'margin-top': '1rem'})
                        ]
                    ),
                    dbc.Input(placeholder="First name", type="name", className="mb-3"),
                    dbc.Input(placeholder="Last name", type="name", className="mb-3"),
                    dbc.Input(placeholder="Email", type="email", className="mb-3"),
                    dbc.Input(placeholder="Password", type="password", className="mb-4"),
                    dbc.Button("Register",
                               color="success",
                               className="w-100 mb-3",
                               href="/newlyRegistered"),

                ]
            )
        )


    elif pathname == "/about":
        return html.Div([
            dbc.Container([
                html.H2("🌍 About E-Mission Possible", className="text-center text-success my-5 fw-bold display-5"),

                dbc.Row([
                    dbc.Col([
                        html.P("""
                    E-Mission Possible is your interactive guide to sustainable travel. 
                    Our mission is to raise awareness about CO₂ emissions and empower individuals 
                    to make informed transportation choices.
                """, className="lead text-muted"),

                        html.P("""
                    Through tools, statistics, and engaging visuals, we help you explore the impact 
                    of your daily commutes and journeys. Whether you're biking, walking, or driving — 
                    we're here to help you understand and reduce your carbon footprint.
                """, className="text-muted"),

                        html.P("""
                    Together, let's make green choices — one trip at a time.
                """, className="text-muted fst-italic"),
                    ], width=10)
                ], justify="center")
            ], className="pb-5")
        ])

    elif pathname == "/contact":
        return html.Div([
            dbc.Container([
                html.H2("📬 Contact Us", className="text-center text-success my-5 fw-bold display-5"),

                dbc.Row([
                    dbc.Col([
                        html.P("Have questions, feedback, or ideas? We’d love to hear from you!", className="text-muted mb-4"),

                        dbc.Form([
                            dbc.Row([
                                dbc.Col(
                                    dbc.Input(type="text", placeholder="Your Name", className="form-control-lg mb-3"),
                                    md=6
                                ),
                                dbc.Col(
                                    dbc.Input(type="email", placeholder="Your Email", className="form-control-lg mb-3"),
                                    md=6
                                )
                            ]),

                            dbc.Textarea(placeholder="Your Message...", className="form-control mb-3", rows=5),

                            dbc.Button("Send Message", color="success", className="mt-2 px-4", size="lg")
                        ])
                    ], md=10)
                ], justify="center")
            ], className="pb-5")
        ])

    elif pathname == "/resources":
        return html.Div([
            html.H2("📘 Educational Resources", className="text-center mt-5 mb-4 fw-bold text-success display-5"),

            dbc.Container([
                dbc.Row([
                    dbc.Col(
                        dbc.Card([
                            dbc.CardImg(src="/assets/Bild2.jpg", top=True, className="img-fluid rounded-top shadow-sm", style={"maxHeight": "180px", "objectFit": "cover"}),
                            dbc.CardBody([
                                html.H5("🌍 The Impact of Transportation", className="card-title text-success fw-semibold"),
                                html.P("Transportation contributes heavily to CO₂, noise, and air pollution. Learn how everyday travel shapes the climate.",
                                       className="card-text small")
                            ])
                        ], className="shadow-sm h-100"),
                        md=6, xl=5, className="mb-4"
                    ),

                    dbc.Col(
                        dbc.Card([
                            dbc.CardImg(src="/assets/Bild3.jpg", top=True, className="img-fluid rounded-top shadow-sm", style={"maxHeight": "180px", "objectFit": "cover"}),
                            dbc.CardBody([
                                html.H5("♻️ Why Sustainable Mobility Matters", className="card-title text-info fw-semibold"),
                                html.P("Biking, walking, and transit help health and planet. See how small shifts lead to big climate wins.",
                                       className="card-text small")
                            ])
                        ], className="shadow-sm h-100"),
                        md=6, xl=5, className="mb-4"
                    )
                ], justify="center"),

                dbc.Row([
                    dbc.Col(
                        dbc.Card([
                            dbc.CardBody([
                                html.H5("🧪 Interactive Learning Tools", className="card-title text-primary fw-bold"),
                                html.P("Explore these tools to better understand your impact and climate-friendly options.", className="small"),
                                html.Ul([
                                    html.Li(html.A("🌡️ Carbon Footprint Calculator", href="https://www.carbonfootprint.com/calculator.aspx", target="_blank", className="link-success")),
                                    html.Li(html.A("🚀 NASA Climate Kids", href="https://climatekids.nasa.gov", target="_blank", className="link-success")),
                                    html.Li(html.A("🗺️ Sustainable Journey Game", href="https://www.cooltheearth.org", target="_blank", className="link-success")),
                                    html.Li(html.A("📈 Emission Dashboard – Our World in Data", href="https://ourworldindata.org/co2-emissions", target="_blank", className="link-success")),
                                ], className="ms-3")
                            ])
                        ], className="shadow-sm h-100"),
                        md=6, xl=5, className="mb-4"
                    ),

                    dbc.Col(
                        dbc.Card([
                            dbc.CardBody([
                                html.H5("📚 Dive Deeper into the Science", className="card-title text-warning fw-bold"),
                                html.P("Ready for expert-level content? These sources provide the full science behind mobility and climate.", className="small"),
                                html.Ul([
                                    html.Li(html.A("🌐 EPA – Transportation & Air Pollution", href="https://www.epa.gov/transportation-air-pollution-and-climate-change", target="_blank", className="link-warning")),
                                    html.Li(html.A("🚉 UN – Sustainable Transport", href="https://www.un.org/en/climatechange/transport", target="_blank", className="link-warning")),
                                    html.Li(html.A("📊 IPCC Reports on Global Climate", href="https://www.ipcc.ch/reports/", target="_blank", className="link-warning")),
                                ], className="ms-3")
                            ])
                        ], className="shadow-sm h-100"),
                        md=6, xl=5, className="mb-4"
                    )
                ], justify="center")

            ], fluid=True, className="px-4 pb-5")
        ])

    elif pathname == "/dashboard":
        monthly_savings = {
            'Months': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                       'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
            'CO2 Saved (kg)': [13, 16, 21, 18, 19, 23,
                               17, 0, 0, 0, 0, 0]
        }

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

        badges = [
            {"name": "Green Starter", "icon": "🌱", "description": "First 10kg CO₂ saved", "earned": True},
            {"name": "Eco Warrior", "icon": "🛡️", "description": "50kg milestone", "earned": True},
            {"name": "Carbon Hero", "icon": "🦸", "description": "100kg CO₂ saved", "earned": True},
            {"name": "Platinum Saver", "icon": "🏆", "description": "200kg CO₂ saved", "earned": False},
            {"name": "Air Ally", "icon": "💨", "description": "1 ton CO₂ saved", "earned": False},
            {"name": "Tree Guardian", "icon": "🌳", "description": "Saved equivalent of 10 planted trees", "earned": False},
            {"name": "Daily Commuter", "icon": "🚌", "description": "30 days of green driving", "earned": True},
            {"name": "Transit Titan", "icon": "🚆", "description": "1 month of daily public transport", "earned": True},
            {"name": "Bike Master", "icon": "🚴", "description": "100km cycled", "earned": False},
            {"name": "Pedal Pioneer", "icon": "🏅", "description": "Ridden 1000 bike kilometers", "earned": False},
        ]

        return html.Div([
            dbc.Container(fluid=True, className="px-0", children=[
                dbc.Row([
                    # Main content area (10/12 width)
                    dbc.Col([
                        # Header section
                        html.Div([
                            html.H2("Your Sustainability Dashboard",
                                    className="text-center mb-3",
                                    style={"font-weight": "bolder", "font-size": "3em"}),
                            html.P("Track your eco-friendly progress with E-Mission Possible",
                                   className="text-center mb-4 text-success",
                                   style={"font-weight": "bold", "font-size": "1.5em"})
                        ], className="container"),

                        # Three environmental metric cards
                        dbc.Container([
                            dbc.Row([
                                # Card 1: CO2 Savings
                                dbc.Col(
                                    dbc.Card(
                                        [
                                            html.Div("🌍", className="text-center display-4 mt-3"),
                                            dbc.CardBody([
                                                html.H4("CO₂ Savings", className="card-title text-center", style={"color": "#008000"}),
                                                html.H2("127 kg", className="text-center my-3"),
                                                html.P("Equivalent to planting 6 trees",
                                                       className="card-text text-center",
                                                       style={"color": "#008000"})
                                            ])
                                        ],
                                        className="h-100",
                                        style={
                                            "border-radius": "15px",
                                            "box-shadow": "0 4px 8px rgba(0,0,0,0.1)",
                                            "border-top": "4px solid #28a745"
                                        }
                                    ),
                                    md=4, className="mb-4"
                                ),

                                # Card 2: Energy Efficiency
                                dbc.Col(
                                    dbc.Card(
                                        [
                                            html.Div("⚡", className="text-center display-4 mt-3"),
                                            dbc.CardBody([
                                                html.H4("Energy Saved", className="card-title text-center", style={"color": "#008000"}),
                                                html.H2("342 kWh", className="text-center my-3"),
                                                html.P("Enough to power a home for 11 days",
                                                       className="card-text text-center",
                                                       style={"color": "#008000"})
                                            ])
                                        ],
                                        className="h-100",
                                        style={
                                            "border-radius": "15px",
                                            "box-shadow": "0 4px 8px rgba(0,0,0,0.1)",
                                            "border-top": "4px solid #ffc107"
                                        }
                                    ),
                                    md=4, className="mb-4"
                                ),

                                # Card 3: Alternative Transport
                                dbc.Col(
                                    dbc.Card(
                                        [
                                            html.Div("🚲", className="text-center display-4 mt-3"),
                                            dbc.CardBody([
                                                html.H4("Green Miles", className="card-title text-center", style={"color": "#008000"}),
                                                html.H2("89 km", className="text-center my-3"),
                                                html.P("Using bikes/public transport instead of cars",
                                                       className="card-text text-center",
                                                       style={"color": "#008000"})
                                            ])
                                        ],
                                        className="h-100",
                                        style={
                                            "border-radius": "15px",
                                            "box-shadow": "0 4px 8px rgba(0,0,0,0.1)",
                                            "border-top": "4px solid #17a2b8"
                                        }
                                    ),
                                    md=4, className="mb-4"
                                )
                            ], justify="center", className="g-4")
                        ], fluid="md"),

                        # CO2 Graph
                        dbc.Container([
                            dbc.Card([
                                dbc.CardHeader("CO₂ Savings Over Time", className="text-success", style={"font-weight": "bold"}),
                                dbc.CardBody([
                                    dcc.Graph(
                                        id='co2-graph',
                                        figure=fig,
                                        config={'displayModeBar': False}
                                    ),
                                    html.P("Your monthly CO₂ savings from sustainable transportation options.",
                                           className="text-muted text-center mt-2")
                                ])
                            ], className="mt-4",
                                style={"border-radius": "15px", "box-shadow": "0 4px 8px rgba(0,0,0,0.1)"})
                        ], fluid="md", className="mb-5")
                    ], width=10),

                    # Badge sidebar (2/12 width)
                    dbc.Col([
                        html.Div(
                            [
                                html.Div(
                                    "Your Badges",
                                    className="text-center fw-bold py-2",
                                    style={
                                        "background": "#28a745",
                                        "color": "white",
                                        "border-radius": "5px 5px 0 0",
                                        "font-size": "1.1rem"
                                    }
                                ),
                                html.Div(
                                    [
                                        html.Div(
                                            [
                                                html.Span(badge["icon"], className="me-2", style={"font-size": "1.8rem"}),
                                                html.Div(
                                                    [
                                                        html.Strong(badge["name"], className="d-block"),
                                                        html.Small(badge["description"], className="text-muted")
                                                    ],
                                                    className="d-inline-block"
                                                )
                                            ],
                                            className="p-3 border-bottom",
                                            style={
                                                "background": "#e8f5e9" if badge["earned"] else "#f8f9fa",
                                                "border-left": "4px solid #28a745" if badge["earned"] else "none",
                                                "transition": "all 0.3s"
                                            }
                                        ) for badge in badges
                                    ],
                                    style={
                                        "background": "#f8f9fa",
                                        "border-radius": "0 0 5px 5px",
                                        "height": "90vh",
                                        "overflow-y": "auto"
                                    }
                                )
                            ],
                            style={
                                "position": "sticky",
                                "top": "20px",
                                "border-radius": "5px",
                                "box-shadow": "0 2px 5px rgba(0,0,0,0.1)",
                                "width": "100%"
                            }
                        )
                    ], width=2, className="pe-0")
                ], className="g-0")
            ])
        ], className="py-4", style={"background-color": "#f8f9fa"})

    elif pathname == "/newlyRegistered":
        monthly_savings = {
            'Months': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                       'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
            'CO2 Saved (kg)': [0, 0, 0, 0, 0, 0,
                               0, 0, 0, 0, 0, 0]
        }

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

        badges = [
            {"name": "Green Starter", "icon": "🌱", "description": "First 10kg CO₂ saved", "earned": False},
            {"name": "Eco Warrior", "icon": "🛡️", "description": "50kg milestone", "earned": False},
            {"name": "Carbon Hero", "icon": "🦸", "description": "100kg CO₂ saved", "earned": False},
            {"name": "Platinum Saver", "icon": "🏆", "description": "200kg CO₂ saved", "earned": False},
            {"name": "Air Ally", "icon": "💨", "description": "1 ton CO₂ saved", "earned": False},
            {"name": "Tree Guardian", "icon": "🌳", "description": "Saved equivalent of 10 planted trees", "earned": False},
            {"name": "Daily Commuter", "icon": "🚌", "description": "30 days of green driving", "earned": False},
            {"name": "Transit Titan", "icon": "🚆", "description": "1 month of daily public transport", "earned": False},
            {"name": "Bike Master", "icon": "🚴", "description": "100km cycled", "earned": False},
            {"name": "Pedal Pioneer", "icon": "🏅", "description": "Ridden 1000 bike kilometers", "earned": False},
        ]

        return html.Div([
            dbc.Container(fluid=True, className="px-0", children=[
                dbc.Row([
                    dbc.Col(
                        dbc.Alert(
                            "There is no data yet. Your road to sustainability starts here!",
                            color="danger"
                        ),
                        width=9,  # 3/4 der Breite
                        className="mx-auto"  # Zentriert die Spalte
                    ),
                ]),

                dbc.Row([
                    # Main content area (10/12 width)
                    dbc.Col([
                        # Header section
                        html.Div([
                            html.H2("Your Sustainability Dashboard",
                                    className="text-center mb-3",
                                    style={"font-weight": "bolder", "font-size": "3em"}),
                            html.P("Track your eco-friendly progress with E-Mission Possible",
                                   className="text-center mb-4 text-success",
                                   style={"font-weight": "bold", "font-size": "1.5em"})
                        ], className="container"),

                        # Three environmental metric cards
                        dbc.Container([
                            dbc.Row([
                                # Card 1: CO2 Savings
                                dbc.Col(
                                    dbc.Card(
                                        [
                                            html.Div("🌍", className="text-center display-4 mt-3"),
                                            dbc.CardBody([
                                                html.H4("CO₂ Savings", className="card-title text-center", style={"color": "#008000"}),
                                                html.H2("0 kg", className="text-center my-3"),
                                                html.P("Equivalent to planting 0 trees",
                                                       className="card-text text-center",
                                                       style={"color": "#008000"})
                                            ])
                                        ],
                                        className="h-100",
                                        style={
                                            "border-radius": "15px",
                                            "box-shadow": "0 4px 8px rgba(0,0,0,0.1)",
                                            "border-top": "4px solid #28a745"
                                        }
                                    ),
                                    md=4, className="mb-4"
                                ),

                                # Card 2: Energy Efficiency
                                dbc.Col(
                                    dbc.Card(
                                        [
                                            html.Div("⚡", className="text-center display-4 mt-3"),
                                            dbc.CardBody([
                                                html.H4("Energy Saved", className="card-title text-center", style={"color": "#008000"}),
                                                html.H2("0 kWh", className="text-center my-3"),
                                                html.P("Enough to power a home for 0 days",
                                                       className="card-text text-center",
                                                       style={"color": "#008000"})
                                            ])
                                        ],
                                        className="h-100",
                                        style={
                                            "border-radius": "15px",
                                            "box-shadow": "0 4px 8px rgba(0,0,0,0.1)",
                                            "border-top": "4px solid #ffc107"
                                        }
                                    ),
                                    md=4, className="mb-4"
                                ),

                                # Card 3: Alternative Transport
                                dbc.Col(
                                    dbc.Card(
                                        [
                                            html.Div("🚲", className="text-center display-4 mt-3"),
                                            dbc.CardBody([
                                                html.H4("Green Miles", className="card-title text-center", style={"color": "#008000"}),
                                                html.H2("0 km", className="text-center my-3"),
                                                html.P("Using bikes/public transport instead of cars",
                                                       className="card-text text-center",
                                                       style={"color": "#008000"})
                                            ])
                                        ],
                                        className="h-100",
                                        style={
                                            "border-radius": "15px",
                                            "box-shadow": "0 4px 8px rgba(0,0,0,0.1)",
                                            "border-top": "4px solid #17a2b8"
                                        }
                                    ),
                                    md=4, className="mb-4"
                                )
                            ], justify="center", className="g-4")
                        ], fluid="md"),

                        # CO2 Graph
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
                    ], width=10),

                    # Badge sidebar (2/12 width)
                    dbc.Col([
                        html.Div(
                            [
                                html.Div(
                                    "Your Badges",
                                    className="text-center fw-bold py-2",
                                    style={
                                        "background": "#28a745",
                                        "color": "white",
                                        "border-radius": "5px 5px 0 0",
                                        "font-size": "1.1rem"
                                    }
                                ),
                                html.Div(
                                    [
                                        html.Div(
                                            [
                                                html.Span(badge["icon"], className="me-2", style={"font-size": "1.8rem"}),
                                                html.Div(
                                                    [
                                                        html.Strong(badge["name"], className="d-block"),
                                                        html.Small(badge["description"], className="text-muted")
                                                    ],
                                                    className="d-inline-block"
                                                )
                                            ],
                                            className="p-3 border-bottom",
                                            style={
                                                "background": "#e8f5e9" if badge["earned"] else "#f8f9fa",
                                                "border-left": "4px solid #28a745" if badge["earned"] else "none",
                                                "transition": "all 0.3s"
                                            }
                                        ) for badge in badges
                                    ],
                                    style={
                                        "background": "#f8f9fa",
                                        "border-radius": "0 0 5px 5px",
                                        "height": "90vh",
                                        "overflow-y": "auto"
                                    }
                                )
                            ],
                            style={
                                "position": "sticky",
                                "top": "20px",
                                "border-radius": "5px",
                                "box-shadow": "0 2px 5px rgba(0,0,0,0.1)",
                                "width": "100%"
                            }
                        )
                    ], width=2, className="pe-0")
                ], className="g-0")
            ])
        ], className="py-4", style={"background-color": "#f8f9fa"})

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
