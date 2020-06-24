from django.urls import path

from . import views

urlpatterns = [

    path("",views.index, name="index"),
    path("login",views.login, name="login"),
    path("add_sport",views.add_sport, name="add_sport"),
    path("edit_sport",views.edit_sport, name="edit_sport"),
    path("view_sport",views.edit_sport, name="view_sport"),
    

]
