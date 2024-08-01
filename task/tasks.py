from celery import shared_task
from datetime import datetime, timedelta
from django.utils import timezone
from .models import ClientAppointment
from .utilities import custom_email_sender


@shared_task
def send_reminders():
    now = timezone.now()

    one_day_ahead = now + timedelta(days=1)
    one_hour_ahead = now + timedelta(hours=1)

    # Find out appointments one day ahead
    appointments_one_day = ClientAppointment.objects.filter(
        appointment_date=one_day_ahead.date(),
        appointment_time__hour=one_hour_ahead.time().hour,
        appointment_time__minute=one_day_ahead.time().minute

    )

    appointments_one_hour = ClientAppointment.objects.filter(
        appointment_date=one_day_ahead.date(),
        appointment_time__hour=one_hour_ahead.time().hour,
        appointment_time__minutes=one_hour_ahead.time().minute,

    )


    # Send appoitments notification
    for appointment in appointments_one_day:
        email_subject = 'Reminder: Property inspection.'
        email_message = f"Hello {appointment.first_name}, kindly note that your appointment is coming up on {appointment.appointment_date}, see you there!"
        sender = 'Favour Idowu'
        email_aadress = appointment.email_address
        custom_email_sender(email_aadress, email_subject, email_message, sender)


    for appointment in appointments_one_hour:
        email_subject = 'Reminder: Property inspection.'
        email_message = f"Hello {appointment.first_name}, kindly note that your appointment is about to start in an hour, see you there!"
        sender = 'Favour Idowu'
        email_aadress = appointment.email_address
        custom_email_sender(email_aadress, email_subject, email_message, sender)
        