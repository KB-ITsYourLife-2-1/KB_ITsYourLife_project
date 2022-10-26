from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import schedule_api1, schedule_api2, schedule_api3

def start():
    scheduler = BackgroundScheduler(timezone='Asia/Seoul')
    # day_of_week 0=월 6=일
    # 설정한 시간에 한번씩 실행됨
    @scheduler.scheduled_job('cron', hour='13', minute='00', id='test_1')
    def job1():
        schedule_api1()

    @scheduler.scheduled_job('cron', hour='14', minute='00', id='test_2')
    def job2():
        schedule_api2()

    @scheduler.scheduled_job('cron', day_of_week=6, hour='05', minute='00', id='test_3')
    def job3():
        schedule_api3()

    scheduler.start()