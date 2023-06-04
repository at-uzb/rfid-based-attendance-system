from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("home", HomeView, name= "home"),
    path("groups", groupView, name="groups"),
    path("students",studentsView,name='students'),
    path("attendances",attendanceView, name="attendance"),
    path("rooms", RoomView, name="room"),
    path('students/<rfid>', studentView, name='student'),
    path('groups/<gr>', grView, name='group'),
    path('rooms/<rn>', rnView, name="rooms_att"),
    path('searched/', my_form, name='searched')
    
] 