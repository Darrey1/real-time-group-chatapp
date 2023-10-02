from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('send', views.send, name='send'),
    path('<str:room>/', views.room, name='room'),
    path('verify', views.verify, name='verify'),
    path('messages/<str:room>/', views.messages, name='messages'),
]
