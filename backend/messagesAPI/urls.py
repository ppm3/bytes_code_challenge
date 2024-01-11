from django.urls import path
from . import views

urlpatterns = [
    path('messages/', views.message_list),
    path('messages/<int:message_id>/', views.message_detail),
]