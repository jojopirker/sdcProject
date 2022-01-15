import pandas as pd
import dash
from dash import dcc
from dash import html
import plotly.express as px
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import random
# percentage of data points
p = 0.01
base_path = "/dash/"
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP], url_base_pathname=base_path)
# server for deploy
server = app.server


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
## Data preparation
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

#####################
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

def build_default(pathname):
    return html.Div([
        html.H3('You are on page {}'.format(pathname)),
    ])

def build_page_2(pathname):
    return html.Div([
        html.H1(children='Accidents Dashoard'),
        ## ACCIDENTS
        dcc.DatePickerRange(
            id='date-picker-page2',
            min_date_allowed=accidents_monthly.index.min(),
            max_date_allowed=accidents_monthly.index.max(),
            start_date=accidents_monthly.index.min(),
            end_date=accidents_monthly.index.max()
        ),
        dcc.Graph(
            id='line-graph-page2'
        ),
        # MAP WITH INCIDENTS PER DISTRICT
        dcc.Graph(
            id='map-graph-occurances', figure={}
        ),
        # Relation of Speed Limit and Number of Casualaties
        dcc.Graph(
            id='relation-speedlimit-casualties-1', figure={}
        ),
        dcc.Graph(
            id='relation-speedlimit-casualties-2', figure={}
        ),
        ## VEHICLES
        # Vehicles Driver Age/sex Histogram
        dcc.Graph(
            id='vehicles-hist', figure={}
        ),
        # Engine Capacity
        dcc.Graph(
            id='vehicles-capacity', figure={}
        ),
        html.H3('You are on page {}'.format(pathname))
    ])

@app.callback([Output('line-graph-page2', 'figure'),
                Output('map-graph-occurances', 'figure'),
                Output('relation-speedlimit-casualties-1', 'figure'),
                Output('relation-speedlimit-casualties-2', 'figure'),
                Output('vehicles-hist', 'figure'),
                Output('vehicles-capacity', 'figure')],
              [Input(component_id='date-picker-page2', component_property='start_date'),
               Input(component_id='date-picker-page2', component_property='end_date')])
def build_accident_line_chart(start_date, end_date):
    # ACCIDENTS
    accidents_monthly_cache = accidents_monthly[start_date:end_date]
    accidents_monthly_cache.rename(columns={'Accident_Index':'Amount of Accidents'}, inplace=True)

    fig = px.line(
        data_frame = accidents_monthly_cache,
        x=accidents_monthly_cache.index,
        y=['Amount of Accidents','Moving Average']
    )
    fig.update_layout(
        title="Monthly number of accidents with 5 month moving average",
        xaxis_title="Time",
        yaxis_title="Number of Accidents",
        legend_title="Legend"
    )

    accidents_cache = accidents_ts[start_date:end_date]
    fig_map = px.scatter_geo(
        data_frame=accidents_cache,
        lat="Latitude",
        lon="Longitude"
    )
    fig_rel_speed_casualties = px.scatter(accidents_cache.nlargest(20, 'Number_of_Casualties'), 
                 x="Number_of_Casualties", 
                 y="Speed_limit",
                color = "Number_of_Vehicles",
                text="1st_Road_Number")

    accidents_small = accidents_cache[['Day_of_Week','Number_of_Casualties','Speed_limit']].groupby(['Speed_limit','Day_of_Week'],as_index=False).sum()
    accidents_small['Day_of_Week'] = pd.Categorical(accidents_small['Day_of_Week'] , ['Monday', 'Tuesday', 'Wednesday','Thursday','Friday','Saturday','Sunday'])
    accidents_small = accidents_small.pivot(index='Speed_limit', columns='Day_of_Week', values='Number_of_Casualties')

    fig_acc_small = px.imshow(accidents_small)

    # VEHICLES
    fig_hist = px.histogram(vehicles[vehicles["Age_of_Driver"]>0], 
                   x="Age_of_Driver", 
                  color="Sex_of_Driver",
                  nbins=12)

    fig_capacity = px.scatter(vehicles[vehicles['Age_of_Vehicle']>=0].sample(1000, random_state=1), # NEEDS TO BE ADAPTED
                 x="Age_of_Driver", 
                 y="Engine_Capacity_(CC)", 
                 color="Vehicle_Type", 
                 size='Age_of_Vehicle',
                 symbol="Sex_of_Driver")

    return fig, fig_map, fig_rel_speed_casualties, fig_acc_small, fig_hist, fig_capacity

switcher = {
    base_path+"page-2": build_page_2
} 

if __name__ == '__main__':
    app.run_server()