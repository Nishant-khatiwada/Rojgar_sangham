from django.conf import settings
from django.core.mail import send_mail


def send_email_token(email,token):
    try:
        subject = 'Your account needs to be verified'
        message = f'Hi Rojgar Sangam User! You can verify your email address using the link:http://127.0.0.1:8000/{token}/'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail( subject, message, email_from, recipient_list )
    except Exception as e:
        return False
    
    return True
