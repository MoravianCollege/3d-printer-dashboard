import requests


url = 'http://127.0.0.1:5000/objfile?auth='+AUTH_KEY
files = {'file': open('gourd2.obj', 'r')}

r = requests.post(url, files=files)
print(r.text)

files = {'file': open('teapot.obj', 'r')}

r = requests.post(url, files=files)
print(r.text)
