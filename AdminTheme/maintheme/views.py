from django.shortcuts import render
import requests
import json
#Create your views here.
r=None
p=None



def login(request) :
   if (request.method)=="POST":
       uname=request.POST.get('username') 
       pas=request.POST.get('password')
       rme=request.POST.get('customCheck')
       global r 
       global p
       try:
        r = requests.post('https://group-10-api.herokuapp.com/Adminlogin',data={'username':uname,'password':pas})
        p= r.json()['access_token']
        return render(request,'index.html')
       except KeyError:
        return render(request, "login.html")

   return render(request, "login.html")


def index(request) :
    return render(request,"index.html")
   # response=request.post('http://ourlink.com/login',data={'username':user_name.'password':password_})

def add_sport(request) :
    return render(request, "add_sport.html")

def edit_sport(request) :
    return render(request, "edit_sport.html")

def view_sport(request) :
    return render(request, "view_sport.html")






    
