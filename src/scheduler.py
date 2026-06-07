from apscheduler.schedulers.blocking import BlockingScheduler
from main import run_pipeline

scheduler = BlockingScheduler()
scheduler.add_job(run_pipeline, 'interval', hours=24)

run_pipeline()
scheduler.start()
