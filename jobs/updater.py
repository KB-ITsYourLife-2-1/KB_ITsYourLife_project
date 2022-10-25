from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import schedule_api

def start():
    scheduler = BackgroundScheduler(timezone='Asia/Seoul')
    # day_of_week 0=월 6=일
    # 설정한 시간에 한번씩 실행됨
    @scheduler.scheduled_job('cron',day_of_week = 2, hour='12', minute='04', id='test_2')
    def job2():
        schedule_api()

    scheduler.start()