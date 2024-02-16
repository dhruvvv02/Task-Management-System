from django.urls import path
from . import views

urlpatterns=[
    path('',views.allotment,name='index'),
    path('submit-form/', views.submit_form, name='submit_form'),
    
]