import sys
import requests
import json

URL = 'http://127.0.0.1:8000/test9/'

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

    # human : C:/Users/Gain/Desktop/NewEGAT/results/225061.jpg
    # cat : C:/Users/Gain/Desktop/NewEGAT/results/3412.jpg
    # snake : C:/Users/Gain/Desktop/NewEGAT/results/1234412312.jpg

data = {"csrfmiddlewaretoken":csrftoken, "Intruder":"SNAKE", "Ipcamera":"CAM003", "Time":"08/02/2020 02:01PM", "ImageID":"1234412312.jpg"}
r = client.post(URL, data=data, headers={"Referer":URL})