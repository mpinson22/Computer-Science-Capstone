#################################################
# AppLayout.py                                  #
#                                               #
# Contains the Dash code for the HTML interface #
#################################################
from dash import Dash

from dash import dcc
from dash import html

from dash import dash_table
from dash import Input, Output, ctx, State

import pandas as pd

from ButtonStyles import *

from CRUD import CourseCatalog

import base64

username = "student"
password = "courseLogin"
university = CourseCatalog(username, password)

# class read method must support return of list object and accept projection json input
# sending the read method an empty document requests all documents be returned
df = pd.DataFrame.from_records(university.readCourse({}))

# MongoDB v5+ is going to return the '_id' column and that is going to have an
# invalid object type of 'ObjectID' - which will cause the data_table to crash - so we remove
# it in the dataframe here. The df.drop command allows us to drop the column. If we do not set
# inplace=True - it will return a new dataframe that does not contain the dropped column(s)
df.drop(columns=['registered', 'Class ID', 'Time', '_id'], inplace=True, axis=1)

visible = {'display':'flex', 'flex-direction':'row', 'justify-content':'space-around', 'flex-wrap':'wrap'}
invisible = {'display':'none'}

image_filename = 'app-logo-small.png'
encoded_image = base64.b64encode(open(image_filename, 'rb').read())

layout = html.Div(style={'font-family':'Georgia'}, children=[
    html.Div(id='hidden-div', style=invisible),
    html.Center(html.A(html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()), 
                                height = 75, width = 75), target = "_blank")),
    html.Center(html.B(html.H1('ABCU Course Catalog'))),
    html.Hr(),
    html.Div(className='buttonRow',
             style={'display': 'flex'},
             children=[
                 html.Button(id='major-button-one', n_clicks_timestamp=-1, n_clicks=0,
                             children='Architecture', style=major_button_style),
                 html.Button(id='major-button-two', n_clicks_timestamp=-1, n_clicks=0,
                             children='Education', style=major_button_style),
                 html.Button(id='major-button-three', n_clicks_timestamp=-1, n_clicks=0,
                             children='Engineering', style=major_button_style),
                 html.Button(id='major-button-four', n_clicks_timestamp=-1, n_clicks=0,
                             children='Environmental Studies', style=major_button_style),
                 html.Button(id='major-button-five', n_clicks_timestamp=-1, n_clicks=0,
                             children='Information', style=major_button_style)]),
    html.Div(className='buttonRow',
             style={'display': 'flex'},
             children=[
                 html.Button(id='major-button-six', n_clicks_timestamp=-1, n_clicks=0,
                             children='Kinesiology', style=major_button_style),
                 html.Button(id='major-button-seven', n_clicks_timestamp=-1, n_clicks=0,
                             children='Medicine', style=major_button_style),
                 html.Button(id='major-button-eight', n_clicks_timestamp=-1, n_clicks=0,
                             children='Performing Arts', style=major_button_style),
                 html.Button(id='major-button-nine', n_clicks_timestamp=-1, n_clicks=0,
                             children='Nursing', style=major_button_style),
                 html.Button(id='major-button-ten', n_clicks_timestamp=-1, n_clicks=0,
                             children='Pharmacy', style=major_button_style)]),
    html.Div(className='buttonRow',
             style={'display': 'flex'},
             children=[
                 html.Button(id='all-button', n_clicks_timestamp=-1, n_clicks=0,
                             children='All Courses', style=all_clicked_style)]),
    html.Br(),
    dash_table.DataTable(
        id='datatable-id',
        columns=[
            {"name": str(i), "id": str(i), "deletable": False, "selectable": False} for i in df.columns
        ],
        data=df.to_dict('records'),
        editable=False,
        filter_action="native",
        sort_action="native",
        sort_mode="multi",
        column_selectable=False,
        row_selectable="multi",
        row_deletable=False,
        selected_columns=[],
        selected_rows=[],
        page_action="native",
        page_current=0,
        page_size=10,
        style_cell={'text_align': 'center', 'font-family': 'Georgia', 'background-color': 'rgb(211,248,253)'},
        style_header={'font-weight': 'bold'}
    ),
    html.Div(className='buttonRow',
             style={'display':'flex', 'justify-content':'center'},
             children=[html.Button(id='reset-button', n_clicks_timestamp=-1, n_clicks=0,
                                   children='Reset Course Selections', style=reset_button_style)]),
    html.Hr(),
    html.Br(),
    html.Div([
        html.Center(html.H2("Enter course to search for by registration code:"), style={'font-family': 'Georgia'}),
        html.Center(dcc.Input(id='subject-code',
                              type='text',
                              minLength='2',
                              maxLength='8',
                              pattern='[a-z][A-Z]{2-8}',
                              placeholder='Enter course subject code',
                              style={'font-size': '20px', 'font-family': 'Georgia', 'width': '30%'})),
        html.Center(dcc.Input(id='course-number',
                              type='number',
                              min=100,
                              max=999,
                              placeholder='Enter course number',
                              style={'font-size': '20px', 'font-family': 'Georgia', 'width': '30%'})),
        html.Br(),
        html.Center(html.Button(id='search-button', n_clicks_timestamp=-1, n_clicks=0,
                                children='Search', style=other_button_style)),
        html.Br(),
        html.Center(html.Div(id='search-bar-output', style={'font-family': 'Georgia', 'font-size': '25px'})),
        html.Br(),
        html.Center(html.Div(id='course-data', style={'font-family': 'Georgia', 'font-size': '40px'})),
        html.Br(),
        html.Center(dcc.Input(id='first-name',
                              type='text',
                              minLength='2',
                              maxLength='10',
                              pattern='[a-z][A-Z]{2-10}',
                              placeholder='first name',
                              style={'font-size': '20px', 'font-family': 'Georgia', 'width': '30%', 'text-transform':'uppercase'})),
        html.Center(dcc.Input(id='last-name',
                              type='text',
                              minLength='2',
                              maxLength='15',
                              pattern='[a-z][A-z]-{2-15}',
                              placeholder='last name',
                              style={'font-size': '20px', 'font-family': 'Georgia', 'width': '30%', 'text-transform':'uppercase'})),
        html.Center(dcc.Input(id='student-id',
                              type='text',
                              placeholder='Student ID',
                              inputMode='numeric',
                              pattern='[0-9]{7}',
                              maxLength='7',
                              minLength='7',
                              style={'font-size': '20px', 'font-family': 'Georgia', 'width': '30%'})),
        html.Br(),
        html.Center([html.Button(id='registration-button', n_clicks_timestamp=-1, n_clicks=0, disabled=True,
                                 children='Register', style=other_button_style),
                     html.Button(id='deregistration-button', n_clicks_timestamp=-1, n_clicks=0, disabled=True,
                                 children='Deregister', style=other_button_style)]),
        html.Br(),
        html.Center(html.Div(id='register-text')),
        html.Br(),
        html.Center(html.Button(id='create-student', n_clicks_timestamp=-1, n_clicks=0, hidden='hidden',
                               children='Create Student Account', style=other_button_style)),
        html.Br(),
        html.Center(html.Div(id='create-student-text'))]),
    html.Br(),
    html.Hr(),
    html.Center(dcc.RadioItems(id='audit-choice', 
                                   options=['Architecture', 'Education', 'Engineering', 'Environmental Studies', 'Information',
                                            'Kinesiology', 'Medicine', 'Performing Arts', 'Nursing', 'Pharmacy'], 
                                   value=None, 
                                   inline=True)),
    html.Br(),
    html.Center(html.Button(id='audit-button', children='Run Degree Audit', n_clicks_timestamp=-1, n_clicks=0, 
                                style=other_button_style)),
    html.Br(),
    html.Div(id='audit-completion', style=invisible, children=[html.H2("Degree Completion", style={'flex-grow':1}), 
                                                    html.H2("Audit Report", style={'flex-grow':1})]),
    html.Hr(),
    html.Div(id='audit-remaining', style=invisible, children=[dcc.Graph(id="completion", style={'flex-grow':1}),
                                                     dcc.Graph(id="remaining", style={'flex-grow':1})]),
    html.Br(),
    html.Hr()
])