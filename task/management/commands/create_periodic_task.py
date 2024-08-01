# your_app/management/commands/create_periodic_task.py
from django.core.management.base import BaseCommand
from django_celery_beat.models import PeriodicTask, CrontabSchedule
from datetime import datetime

class Command(BaseCommand):
    help = 'Create a periodic task to send reminders every minute'

    def handle(self, *args, **kwargs):
        schedule, created = CrontabSchedule.objects.get_or_create(minute='*/1')
        PeriodicTask.objects.create(
            crontab=schedule,
            name='Send Reminder Every Minute',
            task='appointment_task_manager.tasks.send_reminders',
            start_time=datetime.now()
        )
        self.stdout.write(self.style.SUCCESS('Successfully created periodic task'))
