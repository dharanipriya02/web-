from django.urls import path

from . import views

urlpatterns = [

    path("index",views.index, name="index"),
    path('',views.login, name="login"),
    path("add_sport",views.add_sport, name="add_sport"),
    path("edit_sport",views.edit_sport, name="edit_sport"),
    path("view_sport",views.edit_sport, name="view_sport"),
    

]
