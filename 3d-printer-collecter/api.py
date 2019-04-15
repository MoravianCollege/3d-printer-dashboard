
from flask import Flask,request,render_template
import json
from sql import sql

app = Flask(__name__)

sql=sql()


@app.route('/')
def blank():
    return json.dumps({})


# Gets a number of jobs depending on the limit given.
@app.route('/get_jobs')
def job_list():
    limit = request.args.get('limit', '')
    if limit=='':
        limit='20'
    limit=int(limit)

    results=sql.query()
    if limit==0:
        return json.dumps({})
    if limit>len(results):
        return json.dumps(results)

    else:
        return json.dumps(results[:limit])


# Gets stats for the most recent job on specified printer
@app.route('/get_display_stats')
def display_stats():
    printer = request.args.get('printer', '')
    results = sql.query()
    data = []
    for result in results:
        if result['details']['printer'] == printer:
            if result['details']['status'] != 'finished':
                data.append(result)

    return json.dumps(data)


# allows for a http post to save a json file locally
@app.route('/objfile',methods = ['POST'])
def post_obj():
    auth = request.args.get('auth', '')
    if request.method == 'POST':
        if auth == '' or auth != 'AUTH_KEY':
            return 'Wrong or no key'
        if auth == '2SY7ePp$X{J`x@c':
            file = request.get_data()
            file = file.decode()
            file_list = file.split()
            filename = file_list[4][10:len(file_list[4])-1]
            f = open("static/objfiles/"+filename, "w")
            f.write(file[93+len(filename)+1:len(file)-40])
            return 'uploaded: '+ filename


if __name__ == '__main__':
    app.run(debug=True)
