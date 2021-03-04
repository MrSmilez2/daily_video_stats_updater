from __future__ import absolute_import, unicode_literals
from celery import shared_task
from celery.schedules import crontab
from .database_update_logic.daily_content_update import create_daily_video_stat

import time

@shared_task
def collect_daily_video_stat():
    create_daily_video_stat()


SCHEDULE = {
    "video_information_update": {
        "task": "youtube_databasea.tasks.collect_daily_video_stat",
        "args": (),
        "options": {},
        "schedule": crontab(minute=37, hour=20),
    }
}

