import requests
import json
import texttable as tt
import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
import pandas as pd


filenames=[]
printer=[]
date_started=[]
date_finished=[]
time_elapsed=[]
status=[]
extruder1_temp=[]
extruder2_temp=[]
bedtemp=[]
data_gutenberg=requests.get('http://127.0.0.1:5000/get_display_stats?printer=gutenberg')
data_gutenberg=json.loads(data_gutenberg.text)
if data_gutenberg == []:
    filenames.append('')
    printer.append('')
    date_started.append('')
    date_finished.append('')
    time_elapsed.append('')
    status.append('')
    extruder1_temp.append('')
    extruder2_temp.append('')
    bedtemp.append('')
else:
    for names in data_gutenberg:
        filenames.append(names['filename'])
        printer.append(names['details']['printer'])
        date_started.append(names['details']['starttime'])
        date_finished.append(names['details']['endtime'])
        time_elapsed.append(names['details']['time_elapsed'])
        status.append(names['details']['status'])
        extruder1_temp.append(str(names['details']['extruder1_temp']))
        extruder2_temp.append(str(names['details']['extruder2_temp']))
        bedtemp.append(str(names['details']['bedtemp']))
data_xerox=requests.get('http://127.0.0.1:5000/get_display_stats?printer=xerox')
data_xerox=json.loads(data_xerox.text)
if data_xerox == []:
    filenames.append('')
    printer.append('')
    date_started.append('')
    date_finished.append('')
    time_elapsed.append('')
    status.append('')
    extruder1_temp.append('')
    extruder2_temp.append('')
    bedtemp.append('')
else:
    for names in data_xerox:
        filenames.append(names['filename'])
        printer.append(names['details']['printer'])
        date_started.append(names['details']['starttime'])
        date_finished.append(names['details']['endtime'])
        time_elapsed.append(names['details']['time_elapsed'])
        status.append(names['details']['status'])
        extruder1_temp.append(str(names['details']['extruder1_temp']))
        extruder2_temp.append(str(names['details']['extruder2_temp']))
        bedtemp.append(str(names['details']['bedtemp']))



headings=('Filenames','Printer','Date Started','Date Finished','Time Elapsed','Status')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
colors ={
    'background': '#111111',
    'text': '#ffffff',
    'gutenberg':'rgb(0, 0, 255)',
    'xerox': 'rgb(255, 111, 50)'

}

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    style={'backgroundColor': colors['background']},
    children=[


    dcc.Textarea(
        value='Gutenberg',
        disabled=True,
        readOnly=True,
        style={'color':colors['text'],'float':'left','backgroundColor': colors['background'],'width': '630',
               'height':'50','font-size':'25','text-align':'center','border-color': colors['background']}
    ),

    dcc.Textarea(
        value='Xerox',
        readOnly=True,
        style={'color':colors['text'],'float':'right','backgroundColor': colors['background'],'width': '630',
               'height':'50','font-size':'25','text-align':'center','border-color':colors['background']}
    ),



    dcc.Textarea(
        placeholder='',
        readOnly=True,
        value=status[0],
        style={'width': '315', 'height':'200','font-size':'25','text-align':'center','vertical-align':'middle',
               'border-color': colors['background'],'backgroundColor':colors['gutenberg'],'color':colors['text']}
    ),
    dcc.Textarea(
        placeholder='',
        readOnly=True,
        value=filenames[0],
        style={'width': '315', 'height': '200', 'font-size': '25', 'text-align': 'center', 'vertical-align': 'middle',
               'border-color': colors['background'],'backgroundColor':colors['gutenberg'],'color':colors['text']}
    ),
    dcc.Textarea(
        placeholder='',
        readOnly=True,
        value=status[1],
        style={'width': '315', 'height': '200', 'font-size': '25', 'text-align': 'center', 'vertical-align': 'middle',
               'border-color': colors['background'],'backgroundColor':colors['xerox'],'color':colors['text']}
    ),
    dcc.Textarea(
        placeholder='',
        readOnly=True,
        value=filenames[1],
        style={'width': '315', 'height': '200', 'font-size': '25', 'text-align': 'center', 'vertical-align': 'middle',
               'border-color':colors['background'],'backgroundColor':colors['xerox'],'color':colors['text']}
    ),
    dcc.Textarea(
        placeholder='',
        readOnly=True,
        value=date_started[0] + '\n' + date_finished[0],
        style={'width': '315', 'height': '200', 'font-size': '25', 'text-align': 'center', 'vertical-align': 'middle',
               'border-color': colors['background'],'backgroundColor':colors['gutenberg'],'color':colors['text']}
    ),
    dcc.Textarea(
        placeholder='',
        readOnly=True,
        value=time_elapsed[0],
        style={'width': '315', 'height': '200', 'font-size': '25', 'text-align': 'center', 'vertical-align': 'middle',
               'border-color': colors['background'],'backgroundColor':colors['gutenberg'],'color':colors['text']}
    ),
    dcc.Textarea(
        placeholder='',
        readOnly=True,
        value=date_started[0] + '\n' + date_finished[0],
        style={'width': '315', 'height': '200', 'font-size': '25', 'text-align': 'center', 'vertical-align': 'middle',
               'border-color': colors['background'],'backgroundColor':colors['xerox'],'color':colors['text']}
    ),
    dcc.Textarea(
        placeholder='',
        readOnly=True,
        value=time_elapsed[1],
        style={'width': '315', 'height': '200', 'font-size': '25', 'text-align': 'center', 'vertical-align': 'middle',
               'border-color': colors['background'],'backgroundColor':colors['xerox'],'color':colors['text']}
    ),
    dcc.Textarea(
        placeholder='',
        readOnly=True,
        value=extruder1_temp[0] + '\n' + extruder2_temp[0] + '\n' + bedtemp[0],
        style={'width': '315', 'height': '200', 'font-size': '25', 'text-align': 'center', 'vertical-align': 'middle',
               'border-color': colors['background'],'backgroundColor':colors['gutenberg'],'color':colors['text']}
    ),
    dcc.Textarea(
        placeholder='',
        readOnly=True,
        value='This is a TextArea component',
        style={'width': '315', 'height': '200', 'font-size': '25', 'text-align': 'center', 'vertical-align': 'middle',
               'border-color': colors['background'],'backgroundColor':colors['gutenberg'],'color':colors['text']}
    ),
    dcc.Textarea(
        placeholder='',
        readOnly=True,
        value=extruder1_temp[1] + '\n' + extruder2_temp[1] + '\n' + bedtemp[1],
        style={'width': '315', 'height': '200', 'font-size': '25', 'text-align': 'center', 'vertical-align': 'middle',
               'border-color': colors['background'],'backgroundColor':colors['xerox'],'color':colors['text']}
    ),
    dcc.Textarea(
        placeholder='',
        readOnly=True,
        value='This is a TextArea component',
        style={'width': '315', 'height': '200', 'font-size': '25', 'text-align': 'center', 'vertical-align': 'middle',
               'border-color': colors['background'],'backgroundColor':colors['xerox'],'color':colors['text']}
    ),

    dcc.Interval(
        id='interval-component',
        interval= 1 * 6000,
        n_intervals=0
    )
])





if __name__ == '__main__':
    app.run_server(host='0.0.0.0')



