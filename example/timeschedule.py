import schedule
import time
import sys
import requests
import json


#Schedule
def job():
    print('I am working as scheduler....!')
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
        csrftoken = client.cookies['csrftoken']

        # human : C:/Users/Gain/Desktop/NewEGAT/results/225061.jpg
        # cat : C:/Users/Gain/Desktop/NewEGAT/results/3412.jpg
        # snake : C:/Users/Gain/Desktop/NewEGAT/results/1234412312.jpg

    data = {"csrfmiddlewaretoken":csrftoken, "Intruder":"HUMAN", "Ipcamera":"Human Filter", "Time":"08/02/2020 02:01PM", "ImageID":"225061.jpg"}
    r = client.post(URL, data=data, headers={"Referer":URL})
    

def lunch_job():
    print("Take lunch break, time is : 2.30 PM")

def screen_break_job():
    print("Please take a small break, its been an hour seated")


schedule.every(1).minutes.do(job)
#schedule.every().hour.do(screen_break_job)
#schedule.every().day.at("20:56").do(lunch_job)
#schedule.every().monday.do(job)
#schedule.every().wednesday.at("13:15").do(job)
#schedule.every().minute.at(":2").do(job)

while True:
    schedule.run_pending()
    time.sleep(10)