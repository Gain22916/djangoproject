import schedule
import time
from example.models import Simple, Intruder, Errormessage, IPstatus,overviewStatus,daily_feeds

#Schedule
def job():
    print('I am working as scheduler....!')
    sc01 = overviewStatus(id=6, Over_name='HumanFilter', Over_num='0' )
    sc01.save()
    sc02 = overviewStatus(id=6, Over_name='CatFilter', Over_num='0' )
    sc02.save()
    sc03 = overviewStatus(id=6, Over_name='SnakeFilter', Over_num='0' )
    sc03.save()
    

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