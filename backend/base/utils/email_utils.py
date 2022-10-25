from base.strConst import *
from django.core.mail import EmailMessage
from rest_framework_simplejwt.tokens import RefreshToken

def activation_email(user):
    try:
        token = RefreshToken.for_user(user)
        subject = ACTIVATION_ACCOUNT
        body = f"{ACTIVATION_LINK}\n\n"\
            f"{LINK(token)}"
        email = EmailMessage(subject, body, from_email='info@mcm.com', to=[user.email, ])
        email.send()
        return True
    except:
        return False
    
    