import pandas as pd
import dash
from dash import dcc
from dash import html
import plotly.express as px

def get_accidents():
    accidents_full = pd.read_csv('../data/Accidents0514.csv')

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

accidents = get_accidents()


df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")


app = dash.Dash(__name__)

# server for deploy
server = app.server

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),


    
        # represents the URL bar, doesn't render anything
    dcc.Location(id='url', refresh=False),

    dcc.Link('Navigate to "/"', href='/'),
    html.Br(),
    dcc.Link('Navigate to "/page-2"', href='/page-2'),

    # content will be rendered in this element
    html.Div(id='page-content')
    
])

@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    print(pathname)
    if(pathname == "/page-2"):
        return html.Div([
                dcc.Graph(
            id='example-graph',
            figure=fig
        ),
            html.H3('You are on page {}'.format(pathname))
        ])
    return html.Div([
            html.H3('You are on page {}'.format(pathname))
        ])

if __name__ == '__main__':
    app.run_server()