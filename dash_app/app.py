import pandas as pd
import dash
from dash import dcc
from dash import html
import plotly.express as px
import plotly.graph_objects as go
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from flask_caching import Cache
import random
# percentage of data points
p = 0.01
base_path = "/dash/"
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP], url_base_pathname=base_path)
# server for deploy
server = app.server
# cache
#
cache = Cache(app.server, config={
    'CACHE_TYPE': 'filesystem',
    'CACHE_DIR': 'cache-directory'
})
TIMEOUT = 600 

#####################
##
##
##
## Loading Data
##
##
##
#####################

def get_accidents():
    accidents_full = pd.read_csv('../data/Accidents0514.csv', header=0, skiprows=lambda i: i>0 and random.random() > p)

    for name in ['Police_Force',
     'Accident_Severity',
     'Day_of_Week',
     'Local_Authority_(District)',
     'Local_Authority_(Highway)',
     '1st_Road_Class',
     'Road_Type',
     'Junction_Detail',
     'Junction_Control',
     '2nd_Road_Class',
     'Pedestrian_Crossing-Human_Control',
     'Pedestrian_Crossing-Physical_Facilities',
     'Light_Conditions',
     'Weather_Conditions',
     'Road_Surface_Conditions',
     'Special_Conditions_at_Site',
     'Carriageway_Hazards',
     'Urban_or_Rural_Area',
     'Did_Police_Officer_Attend_Scene_of_Accident']:
        accidents_full = read_and_join_description(accidents_full, name)
    return accidents_full

def get_vehicles():
    vehicles_full = pd.read_csv('../data/Vehicles0514.csv', header=0, skiprows=lambda i: i>0 and random.random() > p)

    for name in ['Vehicle_Type',
                 'Towing_and_Articulation',
                 'Vehicle_Manoeuvre',
                 'Vehicle_Location-Restricted_Lane',
                 'Junction_Location',
                 'Skidding_and_Overturning',
                 'Hit_Object_in_Carriageway',
                 'Vehicle_Leaving_Carriageway',
                 'Hit_Object_off_Carriageway',
                 '1st_Point_of_Impact',
                 'Was_Vehicle_Left_Hand_Drive?',
                 'Journey_Purpose_of_Driver',
                 'Sex_of_Driver',
                 'Age_Band_of_Driver',
                 'Propulsion_Code']:
        vehicles_full = read_and_join_description(vehicles_full, name)
    return vehicles_full

def read_and_join_description(df, col_name):
    col_name_new = col_name.replace('_',' ')
    col_name_new = col_name_new.replace('?','')
    
    col_name_new = col_name_new.replace('Pedestrian Crossing-Human Control','Ped Cross - Human')
    col_name_new = col_name_new.replace('Pedestrian Crossing-Physical Facilities','Ped Cross - Physical')
    col_name_new = col_name_new.replace('Weather Conditions','Weather')
    col_name_new = col_name_new.replace('Road Surface Conditions','Road Surface')
    col_name_new = col_name_new.replace('Urban or Rural Area','Urban Rural')
    col_name_new = col_name_new.replace('Did Police Officer Attend Scene of Accident','Police Officer Attend')
    col_name_new = col_name_new.replace('Pedestrian ','Ped ')
    col_name_new = col_name_new.replace('Bus or Coach Passenger','Bus Passenger')
    col_name_new = col_name_new.replace('Casualty Home Area Type','Home Area Type')
    col_name_new = col_name_new.replace('Vehicle Location-Restricted Lane','Vehicle Location')
    col_name_new = col_name_new.replace('Vehicle Leaving Carriageway','Veh Leaving Carriageway')
    col_name_new = col_name_new.replace('Hit Object off Carriageway','Hit Object Off Carriageway')
    col_name_new = col_name_new.replace('Journey Purpose of Driver','Journey Purpose')
    col_name_new = col_name_new.replace('Age Band of Casualty','Age Band')
    col_name_new = col_name_new.replace('Age Band of Driver','Age Band')
    col_name_new = col_name_new.replace('Propulsion Code','Vehicle Propulsion Code')
    col_name_new = col_name_new.replace('Driver Home Area Type','Home Area Type')
    
    excel_data = pd.read_excel(open('../data/Road-Accident-Safety-Data-Guide.xls', 'rb'),sheet_name=col_name_new) 
    excel_data.columns = excel_data.columns.str.lower()
    excel_data = excel_data.add_prefix(col_name+'_')
    
    final_df = pd.merge(df, excel_data, how = 'left', left_on=col_name, right_on=col_name+'_code')
    final_df.drop([col_name+'_code',col_name], axis=1,inplace=True)
    final_df.columns = final_df.columns.str.replace('_label','')
    return final_df

#####################
##
##
##
## Data Preparation
##
##
##
#####################
accidents = get_accidents()
vehicles = get_vehicles()
accidents['accident_time'] = pd.to_datetime(accidents['Date']+' '+accidents['Time'])
accidents_ts = accidents.copy()
accidents_ts.set_index('accident_time', drop=True, inplace=True)
accidents_monthly = accidents_ts.resample('M').agg({'Accident_Index':'size'})
accidents_monthly['Moving Average'] = accidents_monthly.rolling(window=5).mean()

vehicles["Vehicle_Type"].replace({
    "Motorcycle 125cc and under": "Motorcycle 125cc and under", 
    "Motorcycle 50cc and under": "Motorcycle 125cc and under",
    "Motorcycle over 125cc and up to 500cc":"Motorcycle over 125cc",
    "Motorcycle over 500cc": "Motorcycle over 125cc",
    "Taxi/Private hire car": "Car"
}, inplace=True)

#####################
##
##
##
######## Layout 
##
##
##
#####################

app.layout = html.Div(children=[
    #html.H1(children='UK Accidents Dashboard'), class add
    dcc.Location(id='url', refresh=False),
    #dcc.Link('Navigate to "/"', href='/'),
    #html.Br(),
    #dcc.Link('Navigate to "/page-2"', href='/page-2'),
    html.Div(id='page-content')
])

def get_path_function(argument):
    func = switcher.get(argument, build_default)
    return func(argument)

@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    print(pathname)
    return get_path_function(pathname)

#####################
##
##
##
## Dashboard Layouts 
##
##
##
#####################

## Vehicles Dash
def build_default(pathname):
    # Vehicles Driver Age/sex Histogram
    vehicles_hist = dbc.Card(
        [
            dbc.CardBody([
                dbc.Row([
                    dbc.Col(html.H4("Histogram Driver's Age based on Gender", className="card-title"),width=10),
                ]),
                dcc.Graph(
                    id='vehicles-hist', figure={}
                ),
            ]),
        ]
    )
    # Engine Capacity
    vehicles_capacity = dbc.Card(
        [
            dbc.CardBody([
                dbc.Row([
                    dbc.Col(html.H4("Age of Driver ~ Engine Capacity", className="card-title"),width=10),
                ]),
                dcc.Graph(
                    id='vehicles-capacity', figure={}
                ),
            ]),
        ]
    )
    # Vehicles Location / Number of Casualties
    vehicles_loc_casualties = dbc.Card(
        [
            dbc.CardBody([
                dbc.Row([
                    dbc.Col(html.H4("Histogram Driver's Age based on Gender", className="card-title"),width=10),
                ]),
                dcc.Graph(
                    id='vehicles-loc-casualties', figure={}
                ),
            ]),
        ]
    )
    # Vehicle Age / Weather
    vehicle_age_weather = dbc.Card(
        [
            dbc.CardBody([
                dbc.Row([
                    dbc.Col(html.H4("Age of Driver ~ Engine Capacity", className="card-title"),width=10),
                ]),
                dcc.Graph(
                    id='vehicles-age-weather', figure={}
                ),
            ]),
        ]
    )
    
    min_eng_cap = int(vehicles['Engine_Capacity_(CC)'].min())
    max_eng_cap = int(vehicles['Engine_Capacity_(CC)'].max())
    return html.Div([
        html.H1(children='Involved Vehicles Dashoard'),
        html.Hr(),
        ## Filter
        dbc.Row([
            # Date Range Filter
            dbc.Col([
                html.H3(children='Vehicle Type'),
                dcc.Dropdown(
                    id='veh-type-multi',
                    options=[
                        {'label': 'Motorcycle 125cc and under', 'value': 'Motorcycle 125cc and under'},
                        {'label': 'Motorcycle over 125cc', 'value': 'Motorcycle over 125cc'},
                        {'label': 'Car', 'value': 'Car'},
                        {'label': 'Minibus (8 - 16 passenger seats)', 'value': 'Minibus (8 - 16 passenger seats)'},
                        {'label': 'Bus or coach (17 or more pass seats)', 'value': 'Bus or coach (17 or more pass seats)'},
                        {'label': 'Ridden horse', 'value': 'Ridden horse'},
                        {'label': 'Agricultural vehicle', 'value': 'Agricultural vehicle'},
                        {'label': 'Tram', 'value': 'Tram'},
                        {'label': 'Van / Goods 3.5 tonnes mgw or under', 'value': 'Van / Goods 3.5 tonnes mgw or under'},
                        {'label': 'Goods over 3.5t. and under 7.5t', 'value': 'Goods over 3.5t. and under 7.5t'},
                        {'label': 'Goods 7.5 tonnes mgw and over', 'value': 'Goods 7.5 tonnes mgw and over'},
                        {'label': 'Mobility scooter', 'value': 'Mobility scooter'},
                        {'label': 'Electric motorcycle', 'value': 'Electric motorcycle'},
                        {'label': 'Other vehicle', 'value': 'Other vehicle'},
                        {'label': 'Motorcycle - unknown cc', 'value': 'Motorcycle - unknown cc'},
                        {'label': 'Goods vehicle - unknown weight', 'value': 'Goods vehicle - unknown weight'},
                        {'label': 'Data missing', 'value': 'Data missing or out of range'},
                    ],
                    value=['Motorcycle 125cc and under', 'Motorcycle over 125cc', 'Car', 'Bus or coach (17 or more pass seats)'],
                    multi=True
                )
            ], width=4),
            # Light Conditions
            dbc.Col([
                html.H3(children='Vehicle Manoeuvre'),
                dcc.Dropdown(
                    id='veh-man-multi',
                    options=[
                        {'label': 'Reversing', 'value': 'Reversing'},
                        {'label': 'Parked', 'value': 'Parked'},
                        {'label': 'Waiting to go / turn', 'value': 'Waiting to go / turn'},
                        {'label': 'Slowing or stopping', 'value': 'Slowing or stopping'},
                        {'label': 'Turning', 'value': 'Turning'},
                        {'label': 'Changing lane', 'value': 'Changing lane'},
                        {'label': 'Overtaking', 'value': 'Overtaking'},
                        {'label': 'Going ahead', 'value': 'Going ahead'},
                        {'label': 'Data missing', 'value': 'Data missing or out of range'},
                    ],
                    value=['Reversing', 'Parked', 'Waiting to go / turn', 'Slowing or stopping', 'Turning', 'Overtaking'],
                    multi=True
                )
            ], width=4),
            # Accident Severity Filter
            dbc.Col([
                html.H3(children='Engine Capacity'),
                dcc.RangeSlider(
                    id='eng-cap-slider',
                    min=min_eng_cap,
                    max=max_eng_cap,
                    step=1,
                    value=[min_eng_cap, max_eng_cap],
                    marks={
                        -1: 'Min',
                        max_eng_cap: 'Max'
                    }
                )
            ], width=3),
        ]),
        html.Br(),
        ## Charts
        dbc.Row([
            dbc.Col(vehicles_hist, width=6),
            dbc.Col(vehicles_capacity, width=6),
        ]),
        html.Br(),
        dbc.Row([
            dbc.Col(vehicles_loc_casualties, width=6),
            dbc.Col(vehicle_age_weather, width=6),
        ]),
        html.Br(),
    ])

## Accidents Dash
def build_page_2(pathname):
    dev_num_incidents = dbc.Card(
        [
            dbc.CardBody([
                dbc.Row([
                    dbc.Col(html.H4("Monthly number of accidents with 5 month moving average", className="card-title"),width=10),
                ]),
                dcc.Graph(id='line-graph-page2', figure={}),
            ]),
        ]
    )
    map_incidents = dbc.Card(
        [
            dbc.CardBody([
                dbc.Row([
                    dbc.Col(html.H4("Incidents in UK", className="card-title"),width=10),
                ]),
                # MAP WITH INCIDENTS
                dcc.Graph(
                    id='map-graph-occurances', figure={}
                ),
            ]),
        ]
    )
    road_weather = dbc.Card(
        [
            dbc.CardBody([
                dbc.Row([
                    dbc.Col(html.H4("Weather and Road Conditions", className="card-title"),width=10),
                ]),
                dcc.Graph(
                    id='weather-road-conditions', figure={}
                ),
            ]),
        ]
    )
    speed_casualties = dbc.Card(
        [
            dbc.CardBody([
                dbc.Row([
                    dbc.Col(html.H4("Top 50 Incidents: Relation Speed Limit ~ Number of Casualties", className="card-title"),width=10),
                ]),
                dcc.Graph(
                    id='relation-speedlimit-casualties-1', figure={}
                ),
            ]),
        ]
    )
    speed_casualties_weekday = dbc.Card(
        [
            dbc.CardBody([
                dbc.Row([
                    dbc.Col(html.H4("Influence of Speed Limit / Weekday on Casualties", className="card-title"),width=10),
                ]),
                dcc.Graph(
                    id='relation-speedlimit-casualties-2', figure={}
                ),
            ]),
        ]
    )

    return html.Div([
        html.H1(children='Accidents Dashoard'),
        html.Hr(),
        ## Filters
        dbc.Row([
            # Date Range Filter
            dbc.Col([
                html.H3(children='Date Range'),
                dcc.DatePickerRange(
                    id='date-picker-page2',
                    min_date_allowed=accidents_monthly.index.min(),
                    max_date_allowed=accidents_monthly.index.max(),
                    start_date=accidents_monthly.index.min(),
                    end_date=accidents_monthly.index.max()
                )
            ], width=3),
            # Accident Severity Filter
            dbc.Col([
                html.H3(children='Accident Severity'),
                dcc.RangeSlider(
                    id='acc-severity-slider',
                    min=1,
                    max=3,
                    step=1,
                    value=[2, 3],
                    marks={
                        1: 'Fatal',
                        2: 'Serious',
                        3: 'Slight'
                    },
                )
            ], width=4),
            # Light Conditions
            dbc.Col([
                html.H3(children='Light Conditions'),
                dcc.Dropdown(
                    id='light-conditions-multi',
                    options=[
                        {'label': 'Daylight', 'value': 'Daylight'},
                        {'label': 'Darkness - lights lit', 'value': 'Darkness - lights lit'},
                        {'label': 'Darkness - lights unlit', 'value': 'Darkness - lights unlit'},
                        {'label': 'Darkness - no lighting', 'value': 'Darkness - no lighting'},
                        {'label': 'Darkness - lighting unknown', 'value': 'Darkness - lighting unknown'},
                        {'label': 'Data missing', 'value': 'Data missing or out of range'}
                    ],
                    value=['Daylight', 'Darkness - lights lit'],
                    multi=True
                )
            ], width=4),
        ]),
        html.Br(),
        ## Charts
        dbc.Row([
            dbc.Col(dev_num_incidents, width=11),
        ]),
        html.Br(),
        dbc.Row([
            dbc.Col(map_incidents, width=5),
            dbc.Col(road_weather, width=6),
        ]),
        html.Br(),
        dbc.Row([
            dbc.Col(speed_casualties_weekday, width=5),
            dbc.Col(speed_casualties, width=6),
        ]),
    ])

## Callback Accident Dash
@app.callback([Output('line-graph-page2', 'figure'),
                Output('map-graph-occurances', 'figure'),
                Output('weather-road-conditions', 'figure'),
                Output('relation-speedlimit-casualties-1', 'figure'),
                Output('relation-speedlimit-casualties-2', 'figure')],
              [Input(component_id='date-picker-page2', component_property='start_date'),
               Input(component_id='date-picker-page2', component_property='end_date'),
               Input(component_id='acc-severity-slider', component_property='value'),
               Input(component_id='light-conditions-multi', component_property='value')])
@cache.memoize(timeout=TIMEOUT)
def build_accident_charts(start_date, end_date, acc_sev, light_con):
    # Filter Date
    accidents_cache=accidents_ts[start_date:end_date]
    # Filter Accident Severity
    acc_sev_dict = {
        1: 'Fatal', 
        2: 'Serious',  
        3: 'Slight'
    }
    acc_sev_trans=[]
    for sev in range(int(acc_sev[0]), int(acc_sev[1])):
        acc_sev_trans.append(acc_sev_dict[sev])
    accidents_cache = accidents_cache[accidents_cache['Accident_Severity'].isin(acc_sev_trans)]
    # Filter Light Conditions
    accidents_cache = accidents_cache[accidents_cache['Light_Conditions'].isin(light_con)]
    # Moving average
    accidents_monthly_cache = accidents_cache.resample('M').agg({'Accident_Index':'size'})
    accidents_monthly_cache['Moving Average'] = accidents_monthly_cache.rolling(window=5).mean()
    accidents_monthly_cache.rename(columns={'Accident_Index':'Amount of Accidents'}, inplace=True)

    fig = px.line(
        data_frame = accidents_monthly_cache,
        x=accidents_monthly_cache.index,
        y=['Amount of Accidents','Moving Average']
    )
    fig.update_layout(
        xaxis_title="Time",
        yaxis_title="Number of Accidents",
        legend_title="Legend"
    )

    fig_map = go.Figure(go.Scattergeo(
        lat=accidents_cache["Latitude"],
        lon=accidents_cache["Longitude"],
        text=accidents_cache["1st_Road_Number"],
        mode="markers",
        marker_color=accidents_cache["Speed_limit"],
    ))
    fig_map.update_geos(
        lataxis_range=[50.10319,60.15456],
        lonaxis_range=[-7.64133,1.75159],
        visible=False, 
        resolution=110, 
        scope="europe",
        showcountries=True, 
        countrycolor="Black",
        showsubunits=True, 
        subunitcolor="Blue"
    )

    accidents_agg = accidents_cache.groupby(['Weather_Conditions','Road_Surface_Conditions'], as_index=False).size()
    fig_weather_road = px.bar(accidents_agg, 
             x='Weather_Conditions', 
             y='size', 
             color='Road_Surface_Conditions', 
             barmode='group')

    fig_rel_speed_casualties = px.scatter(accidents_cache.nlargest(50, 'Number_of_Casualties'), 
        x="Number_of_Casualties", 
        y="Speed_limit",
        color = "Number_of_Vehicles",
        text="1st_Road_Number")

    accidents_small = accidents_cache[['Day_of_Week','Number_of_Casualties','Speed_limit']].groupby(['Speed_limit','Day_of_Week'],as_index=False).sum()
    accidents_small['Day_of_Week'] = pd.Categorical(accidents_small['Day_of_Week'] , ['Monday', 'Tuesday', 'Wednesday','Thursday','Friday','Saturday','Sunday'])
    accidents_small = accidents_small.pivot(index='Speed_limit', columns='Day_of_Week', values='Number_of_Casualties')

    fig_acc_small = px.imshow(accidents_small)

    return fig, fig_map, fig_weather_road, fig_rel_speed_casualties, fig_acc_small

## Callback Vehicles Dash
@app.callback([Output('vehicles-hist', 'figure'),
                Output('vehicles-capacity', 'figure'),
                Output('vehicles-loc-casualties', 'figure'),
                Output('vehicles-age-weather', 'figure')],
              [Input(component_id='veh-type-multi', component_property='value'),
               Input(component_id='eng-cap-slider', component_property='value'),
               Input(component_id='veh-man-multi', component_property='value')])
@cache.memoize(timeout=TIMEOUT)
def build_vehicle_charts(veh_type, eng_cap, veh_man):
    # Filters
    vehicles_cache = vehicles.copy()
    vehicles_cache = vehicles_cache[vehicles_cache['Vehicle_Type'].isin(veh_type)]
    vehicles_cache = vehicles_cache[vehicles_cache['Vehicle_Manoeuvre'].isin(veh_man)]
    vehicles_cache = vehicles_cache[vehicles_cache['Engine_Capacity_(CC)'].between(int(eng_cap[0]), int(eng_cap[1]))]
    # Join
    accidents_vehicles = accidents_ts.join(vehicles_cache.set_index('Accident_Index'))

    # Charts
    fig_hist = px.histogram(vehicles_cache[vehicles_cache["Age_of_Driver"]>0], 
                x="Age_of_Driver", 
                color="Sex_of_Driver",
                nbins=12)

    fig_capacity = px.scatter(vehicles_cache[vehicles_cache['Age_of_Vehicle']>=0], # NEEDS TO BE ADAPTED
                x="Age_of_Driver", 
                y="Engine_Capacity_(CC)", 
                #color="Vehicle_Type", 
                #size='Age_of_Vehicle',
                color="Sex_of_Driver", 
                symbol="Sex_of_Driver")

    # Vehicles Manoeuvre / Number of Casualties
    vehicles_agg = accidents_vehicles.groupby(['Vehicle_Manoeuvre', 'Sex_of_Driver'], as_index=False).sum()
    fig_loc_cas = px.bar(vehicles_agg, 
             x='Vehicle_Manoeuvre', 
             y='Number_of_Casualties', 
             color='Sex_of_Driver', 
             barmode='group')

    # Vehicle Age / Weather
    vehicles_agg = accidents_vehicles.groupby(['Weather_Conditions'], as_index=False).mean()
    fig_age_weather = px.bar(accidents_vehicles, 
             x='Weather_Conditions', 
             y='Age_of_Vehicle', 
             color='Weather_Conditions', 
             barmode='group')

    return fig_hist, fig_capacity, fig_loc_cas, fig_age_weather


switcher = {
    base_path+"page-2": build_page_2
} 

if __name__ == '__main__':
    app.run_server()