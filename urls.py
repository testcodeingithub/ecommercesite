from django.urls import path
from .views import *

urlpatterns = [

path ('',home,name= "app_home"),
path ('login/',login,name= "app_login"),
path ('contact/',contact,name= "app_contact"),
path ('about/',about,name= "app_about"),
path ('search/',search,name= "app_search"),
path ('cart/',cart,name= "app_cart"),

  
]