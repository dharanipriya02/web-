from django.shortcuts import render
import requests
import json
#Create your views here.
r=None
p=None
def index(request) :
    return render(request,"index.html")
   # response=request.post('http://ourlink.com/login',data={'username':user_name.'password':password_})



def login(request) :
   if (request.method)=="POST":
       uname=request.POST.get('username') 
       pas=request.POST.get('password')
       rme=request.POST.get('customCheck')
       global r 
       global p
       try:
           print("heyy")
           r = requests.post('https://group-10-api.herokuapp.com/Adminlogin',data={'username':uname,'password':pas})
           print("hello")
           p= r.json()['access_token']
       except ValueError:
           print("hellooo")

            

       if(p!=None):
        	return render(request,"index.html",{})
   return render(request, "login.html")
def add_sport(request) :
    return render(request, "add_sport.html")

def edit_sport(request) :
    return render(request, "edit_sport.html")

def view_sport(request) :
    return render(request, "view_sport.html")






    
