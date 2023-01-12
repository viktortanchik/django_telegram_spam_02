import schedule

from datetime import datetime, timedelta, time
import time


def job():
    print('Hello World')


#schedule.every(5).seconds.until(timedelta(seconds=20)).do(job)
schedule.every(2).days("2023-01-11 3:59").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)