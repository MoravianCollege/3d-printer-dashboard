import requests
import json
import texttable as tt




data=requests.get('http://127.0.0.1:5000/get_jobs?limit=10')
data=json.loads(data.text)
filenames=[]
printer=[]
date_started=[]
date_finished=[]
time_elapsed=[]
status=[]
for names in data:
    filenames.append(names['filename'])
    printer.append(names['details']['printer'])
    date_started.append(names['details']['starttime'])
    date_finished.append(names['details']['endtime'])
    time_elapsed.append(names['details']['time_elapsed'])
    status.append(names['details']['status'])



tab = tt.Texttable()
headings=['Filenames','Printer','Date Started','Date Finished','Time Elapsed','Status']
tab.header(headings)
filenames = filenames
printer = printer
date_started = date_started
date_finished = date_finished
time_elapsed = time_elapsed
status = status

for row in zip(filenames,printer,date_started,date_finished,time_elapsed,status):
    tab.add_row(row)

s = tab.draw()
print(s)

# print('')
# print('')
#
# data=requests.get('http://10.76.100.145:5000/get_jobs?limit=1')
# data=json.loads(data.text)
# filenames=[]
# printer=[]
# date_started=[]
# date_finished=[]
# time_elapsed=[]
# status=[]
# for names in data:
#     filenames.append(names['filename'])
#     printer.append(names['details']['printer'])
#     date_started.append(names['details']['starttime'])
#     date_finished.append(names['details']['endtime'])
#     time_elapsed.append(names['details']['time_elapsed'])
#     status.append(names['details']['status'])
#
#
#
# tab = tt.Texttable()
# headings=['Filenames','Printer','Date Started','Date Finished','Time Elapsed','Status']
# tab.header(headings)
# filenames = filenames
# printer = printer
# date_started = date_started
# date_finished = date_finished
# time_elapsed = time_elapsed
# status = status
#
# for row in zip(filenames,printer,date_started,date_finished,time_elapsed,status):
#     tab.add_row(row)
#
# s = tab.draw()
# print (s)



