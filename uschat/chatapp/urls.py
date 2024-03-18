from django.urls import path
from . import views

urlpatterns = [
    path('', views.rooms),
    path("<str:slug>/", views.room,name="room"),
]
