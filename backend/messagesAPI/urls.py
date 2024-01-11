from django.urls import path
from . import views

urlpatterns = [
    path('ping', views.ping, name='ping'),
    path('health-check', views.health_check, name='health_check'),
    path('messages/', views.message_list, name='message_list'),
    path('messages/<message_id>/', views.message_detail, name='message_detail'),
]