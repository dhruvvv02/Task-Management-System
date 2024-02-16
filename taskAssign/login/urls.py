from django.urls import path
from . import views

urlpatterns=[
    path('showform/',views.login,name='login'),
    path('getform/',views.getform,name='getform'),
    path('',views.index,name='index'),
]