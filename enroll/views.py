import email
from email.policy import default
from pyexpat.errors import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render

from enroll.forms import StudentRegistartion
from enroll.models import User

from .celery.task import sleepy


# Create your views here.
#this function is for adding new item an show item
def add_show(request):
    if request.method == 'POST':
     fm = StudentRegistartion(request.POST)
     if fm.is_valid():
        nm=fm.cleaned_data['name']
        em=fm.cleaned_data['email']
        pw=fm.cleaned_data['password']
        reg=User(name=nm,email=em,password=pw)
        reg.save()
        fm = StudentRegistartion() 
            
    # we can use this method also fm.save()
    else:    
     fm = StudentRegistartion()
    # stud ko else ke baher lagana chahiye
    stud = User.objects.all()
    # for signal printing at frontend
    ro = request.session.get('ip', 0)
    # for celery
    sleepy.delay(5)
    # sleepy(10)
    return render(request,'enroll/addshow.html',{'form':fm,'stu':stud,'ros':ro})

#update
def update(request,id):
    if request.method =="POST":
        pi=User.objects.get(pk=id)
        fm=StudentRegistartion(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=User.objects.get(pk=id)
        fm=StudentRegistartion(instance=pi) 
    return render(request,'enroll/update.html',{'form':fm})
    # request.method =="POST":
        






# delete function
def delete(request,id):
    if request.method == 'POST':
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
    
    
    
