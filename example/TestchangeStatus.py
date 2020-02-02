import sys
import requests
import json

URL = 'http://127.0.0.1:8000/test43/'

client = requests.session()

# Retrieve the CSRF token first
client.get(URL)  # sets cookie
if 'csrftoken' in client.cookies:
    # Django 1.6 and up
    print('csrftoken')
    csrftoken = client.cookies['csrftoken']
else:
    # older versions
    print('csrf')
    csrftoken = client.cookies['csrf']

data = {"csrfmiddlewaretoken":csrftoken, "ErrorTime":"HUMAN", "ErrorID":"CAM009", "ErrorDetail":"24/11/2019 02:01PM" }
# login_data = {"csrfmiddlewaretoken":csrftoken, 'Object-Type':'Human Giant'}
r = client.post(URL, data=data, headers={"Referer":URL})

