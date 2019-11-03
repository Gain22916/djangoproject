import sys
import requests
import json

URL = 'http://127.0.0.1:8000/test13/'

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

data = {"csrfmiddlewaretoken":csrftoken, "Intruder":"IU", "Ipcamera":"CAM666", "Time":"15/03/2019 11:54AM", "ImageID":"C:/Users/Gain/Desktop/NewEGAT/456.jpg"}
# login_data = {"csrfmiddlewaretoken":csrftoken, 'Object-Type':'Human Giant'}
r = client.post(URL, data=data, headers={"Referer":URL})