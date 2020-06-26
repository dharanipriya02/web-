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
  if(p!=None):
    if (request.method)=="POST":
         Sport_id=request.POST.get('Sport_id') 
         Sport_name=request.POST.get('Sport_name') 
         cat=request.POST.get('Sport_category') 
         mini=request.POST.get('min_team_size') 
         maxi=request.POST.get('max_team_size') 
         print(Sport_id,mini)
         a = requests.post('https://group-10-api.herokuapp.com/sportdetails',headers={'Authorization':f'Bearer {p}'},data={'sport_id':Sport_id,'sport_name':Sport_name,'sport_category':cat,'mini_team_size':mini,'max_team_size':maxi})
         print(a)
         return render(request,'add_sport.html')
    else:
        return render(request,'add_sport.html')
  else:
    return render(request,"login.html")

def edit_sport(request) :
    return render(request, "edit_sport.html")

def view_sport(request) :
  if(p!=None):
    b = requests.get('https://group-10-api.herokuapp.com/sportdetails',headers={'Authorization':f'Bearer {p}'},data={'sport_name':'carroms'})
    carroms = b.json()
    d = requests.get('https://group-10-api.herokuapp.com/sportdetails',headers={'Authorization':f'Bearer {p}'},data={'sport_name':'football'})
    football = d.json()
    return render(request, "view_sport.html",{'carroms':carroms[0],'football':football[0]})
  else:
    return render(request,"login.html")






    
