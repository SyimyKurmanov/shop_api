from  django.core.mail import send_mail
from . celery import app
from account.send_mail import send_confirmation_email

from account.send_mail import send_notification

from account.models import Spam_Contacts


@app.task
def send_confirm_email_task(user, code):
    send_confirmation_email(user, code)

@app.task
def send_notification_task(user_email, order_id, price):
    send_notification(user_email, order_id, price)

@app.task
def send_spam_email():
    for user in Spam_Contacts.objects.all():
        send_mail(
            'SPAM SPAM SPAM',
            'THIS IS SPAM LETTER FOR YOU FROM JOHN SNOW!',
            'syimyk.kurmanov@gmail.com',
            [user.email],
            fail_silently=False,
        )