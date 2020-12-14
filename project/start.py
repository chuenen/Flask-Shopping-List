import time

from apscheduler.schedulers.background import BackgroundScheduler

from . import config
from .app import create_app
from .notifier import main

application = create_app(config)

time.sleep(15)  # Wait for DB

scheduler = BackgroundScheduler()
scheduler.add_job(
    main,
    trigger='interval',
    seconds=config.seconds,
)
scheduler.start()


# vi:et:ts=4:sw=4:cc=80
