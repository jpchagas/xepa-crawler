from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
import os

app = Flask(__name__)

sched = BackgroundScheduler(daemon=True)

count = 0


def run_spider():
    sched.print_jobs()
    os.chdir(os.getcwd() + "/xepacrawler")
    os.system('scrapy crawl ceasars')


sched.add_job(run_spider, 'cron', day='*')
sched.start()

if __name__ == "__main__":
    app.run()
