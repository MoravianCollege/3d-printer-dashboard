import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import json
import requests
import ObjObject


filenames = []
printer = []
date_started = []
date_finished = []
time_elapsed = []
status = []
extruder1_temp = []
extruder2_temp = []
bedtemp = []
data_gutenberg = requests.get('http://127.0.0.1:5000/get_display_stats?printer=gutenberg')
data_gutenberg = json.loads(data_gutenberg.text)
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
data_xerox = requests.get('http://127.0.0.1:5000/get_display_stats?printer=xerox')
data_xerox = json.loads(data_xerox.text)
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

headings = ('Filenames', 'Printer', 'Date Started', 'Date Finished', 'Time Elapsed', 'Status')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
colors = {
    'background': '#111111',
    'text': '#ffffff',
    'gutenberg': 'rgb(0, 0, 255)',
    'xerox': 'rgb(255, 111, 50)'

}

obj = ObjObject.ObjObject("https://people.sc.fsu.edu/~jburkardt/data/obj/teapot.obj")
obj2 = ObjObject.ObjObject("https://people.sc.fsu.edu/~jburkardt/data/obj/octahedron.obj")

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    style={'backgroundColor': colors['background']},
    children=[

        dcc.Textarea(
            value='Gutenberg',
            disabled='True',
            readOnly='True',
            style={'resize': 'none', 'color': colors['text'], 'float': 'left', 'backgroundColor': colors['background'], 'width': '630',
                   'height': '50', 'font-size': '25', 'text-align': 'center', 'border-color': colors['background']}
        ),

        dcc.Textarea(
            value='Xerox',
            readOnly=True,
            style={'resize': 'none', 'color': colors['text'], 'float': 'right', 'backgroundColor': colors['background'], 'width': '630',
                   'height': '50', 'font-size': '25', 'text-align': 'center', 'border-color': colors['background']}
        ),

        dcc.Textarea(
            placeholder='',
            readOnly=True,
            value="Status: \n %s" % (status[0]),
            style={'resize': 'none', 'width': '315', 'height': '200', 'font-size': '25', 'text-align': 'center',
                   'vertical-align': 'middle',
                   'border-color': colors['background'], 'backgroundColor': colors['gutenberg'],
                   'color': colors['text']}
        ),

        dcc.Textarea(
            placeholder='',
            readOnly=True,
            value="Filename: \n %s" % (filenames[0]),
            style={'resize': 'none', 'width': '315', 'height': '200', 'font-size': '25', 'text-align': 'center',
                   'vertical-align': 'middle',
                   'border-color': colors['background'], 'backgroundColor': colors['gutenberg'],
                   'color': colors['text']}
        ),

        dcc.Textarea(
            placeholder='',
            readOnly=True,
            value="Status: \n %s" % (status[1]),
            style={'resize': 'none', 'width': '315', 'height': '200', 'font-size': '25', 'text-align': 'center',
                   'vertical-align': 'middle',
                   'border-color': colors['background'], 'backgroundColor': colors['xerox'], 'color': colors['text']}
        ),

        dcc.Textarea(
            placeholder='',
            readOnly=True,
            value="Filename: \n %s" % (filenames[1]),
            style={'resize': 'none', 'width': '315', 'height': '200', 'font-size': '25', 'text-align': 'center',
                   'vertical-align': 'middle',
                   'border-color': colors['background'], 'backgroundColor': colors['xerox'], 'color': colors['text']}
        ),

        dcc.Textarea(
            placeholder='',
            readOnly=True,
            value="Date Started: \n %s \n \n Date finished: \n %s" % (date_started[0], date_finished[0]),
            style={'resize': 'none', 'width': '315', 'height': '200', 'font-size': '25', 'text-align': 'center',
                   'vertical-align': 'middle',
                   'border-color': colors['background'], 'backgroundColor': colors['gutenberg'],
                   'color': colors['text']}
        ),

        dcc.Textarea(
            placeholder='',
            readOnly=True,
            value="Time elapsed: \n %s" % (time_elapsed[0]),
            style={'resize': 'none', 'width': '315', 'height': '200', 'font-size': '25', 'text-align': 'center',
                   'vertical-align': 'middle',
                   'border-color': colors['background'], 'backgroundColor': colors['gutenberg'],
                   'color': colors['text']}
        ),

        dcc.Textarea(
            placeholder='',
            readOnly=True,
            value="Date Started: \n %s \n \n Date finished: \n %s" % (date_started[0], date_finished[0]),
            style={'resize': 'none', 'width': '315', 'height': '200', 'font-size': '25', 'text-align': 'center',
                   'vertical-align': 'middle',
                   'border-color': colors['background'], 'backgroundColor': colors['xerox'], 'color': colors['text']}
        ),

        dcc.Textarea(
            placeholder='',
            readOnly=True,
            value="Time elapsed: \n %s" % (time_elapsed[1]),
            style={'resize': 'none', 'width': '315', 'height': '200', 'font-size': '25', 'text-align': 'center',
                   'vertical-align': 'middle',
                   'border-color': colors['background'], 'backgroundColor': colors['xerox'], 'color': colors['text']}
        ),

        dcc.Textarea(
            placeholder='',
            readOnly=True,
            value="Extruder temp. 1: \n %s \n Extruder temp. 2: \n %s \n Bed temp. : \n %s" % (extruder1_temp[0], extruder2_temp[0], bedtemp[0]),
            style={'resize': 'none', 'display': 'inline-block', 'width': '315', 'height': '200', 'font-size': '25', 'text-align': 'center',
                   'vertical-align': 'middle',
                   'border-color': colors['background'], 'backgroundColor': colors['gutenberg'],
                   'color': colors['text']}
        ),

        dcc.Graph(
            id='OBJ-File-Graph',
            figure={
                'data': [obj.mesh],
                'layout': {
                    'plot_bgcolor': colors['background'],
                    'paper_bgcolor': colors['background'],
                    'margin': {'l': 10, 'b': 20, 't': 0, 'r': 0}
                }
            },
            config={'editable': True, 'scrollZoom': True},
            style={'display': 'inline-block', 'width': '315', 'height': '200', 'vertical-align': 'middle'},
        ),

        dcc.Textarea(
            placeholder='',
            readOnly=True,
            value="Extruder temp. 1: \n %s \n Extruder temp. 2: \n %s \n Bed temp. : \n %s" % (extruder1_temp[1], extruder2_temp[1], bedtemp[1]),
            style={'resize': 'none', 'display': 'inline-block', 'width': '315', 'height': '200', 'font-size': '25', 'text-align': 'center',
                   'vertical-align': 'middle',
                   'border-color': colors['background'], 'backgroundColor': colors['xerox'], 'color': colors['text']}
        ),

        dcc.Graph(
            id='OBJ-File-Graph-2',
            figure={
                'data': [obj2.mesh],
                'layout': {
                    'plot_bgcolor': colors['background'],
                    'paper_bgcolor': colors['background'],
                    'margin': {'l': 10, 'b': 20, 't': 0, 'r': 0}
                }
            },
            config={'editable': True, 'scrollZoom': True},
            style={'display': 'inline-block', 'width': '315', 'height': '200', 'vertical-align': 'middle'},
        ),

        dcc.Interval(
            id='interval-component',
            interval=1 * 6000,
            n_intervals=0
        )
    ])

@app.callback([Output('status_G', 'value'),
                   Output('filename_G','value'),
                   Output('date_G', 'value'),
                   Output('time_G', 'value'),
                   Output('temps_G', 'value'),],
                  [Input('interval-component', 'n_intervals')])
def update_Gutenberg(n):
        data_gutenberg=requests.get('http://127.0.0.1:5000/get_display_stats?printer=gutenberg')
        data_gutenberg=json.loads(data_gutenberg.text)
        if data_gutenberg == []:
            return '','','','',''
        else:
            for names in data_gutenberg:
                return names['details']['status'], names['filename'],\
                        names['details']['starttime']+ '\n' + names['details']['endtime'],\
                        names['details']['time_elapsed'], \
                        str(names['details']['extruder1_temp']) + '\n' + str(names['details']['extruder2_temp']) + '\n' + str(names['details']['bedtemp'])


@app.callback([Output('status_X', 'value'),
                   Output('filename_X','value'),
                   Output('date_X', 'value'),
                   Output('time_X', 'value'),
                   Output('temps_X', 'value'),],
                  [Input('interval-component', 'n_intervals')])
def update_Xerox(n):
        data_xerox = requests.get('http://127.0.0.1:5000/get_display_stats?printer=xerox')
        data_xerox = json.loads(data_xerox.text)
        if data_xerox == []:
            return '','','','',''
        else:
            for names in data_xerox:
                return names['details']['status'], names['filename'],\
                        names['details']['starttime']+ '\n' + names['details']['endtime'],\
                        names['details']['time_elapsed'], \
                        str(names['details']['extruder1_temp']) + '\n' + str(names['details']['extruder2_temp']) + '\n' + str(names['details']['bedtemp'])

if __name__ == '__main__':
    app.run_server(host='0.0.0.0')
