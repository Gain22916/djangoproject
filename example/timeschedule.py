import schedule
import time

def job():
    print('I am working as scheduler....!')

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
    time.sleep(1)