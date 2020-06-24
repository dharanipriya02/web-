from django.shortcuts import render

# Create your views here.

def index(request) :
    return render(request, "index.html")

def login(request) :
    return render(request, "login.html")

def add_sport(request) :
    return render(request, "add_sport.html")

def edit_sport(request) :
    return render(request, "edit_sport.html")

def view_sport(request) :
    return render(request, "view_sport.html")






    
