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

data = {"csrfmiddlewaretoken":csrftoken, "Intruder":"Snake", "Ipcamera":"CAM020", "Time":"22/03/2020 19:47PM", "ImageID":"1234412312.jpg"}
r = client.post(URL, data=data, headers={"Referer":URL})