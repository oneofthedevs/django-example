# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:q_id>', views.details, name='detail'),
    path('<int:q_id>', views.result, name='result'),
    path('<int:q_id>/vote', views.vote, name='vote'),
]

