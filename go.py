#!/usr/bin/env python
import json
import requests
import cgi
import cgitb
cgitb.enable()

print('Content-Type: text/html')
print('')

form=cgi.FieldStorage()
comment=form.getfirst("Comment")

data = {'Comment': comment}

r = requests.post('https://yklp7nqco6.execute-api.us-east-1.amazonaws.com/alpha/execution', json.dumps(data))
print(r.status_code)

data = r.json()
print(data)
