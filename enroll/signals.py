from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import User
from django.dispatch import receiver

# for signals 

@receiver(user_logged_in, sender=User)             
def login_succeess(sender,request,user,**kwargs):
    ip = request.META.get('REMOTE_ADDR')
    request.session['ip'] = ip