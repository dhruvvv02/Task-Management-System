from django.shortcuts import render
import pyrebase
from django.http import HttpResponse

def login(request):
    # return HttpResponse("Welcome to TaskManagement login page")
    return render(request,"login.html")
def getform(request):
    if request.method=="POST":
        Username=request.POST['Username']
        Password=request.POST['password']
    return HttpResponse("UserName:{} Password:{}".format(Username,Password))


def index(request):
    User_name = database.child('Login').child('Username').get().val()
    User_password = database.child('Login').child('Password').get().val()
   
    return render (request,'index.html',{
        "User_name" :User_name,
        "User_password " :User_password,
    })
# new function

config={
 "apiKey": "AIzaSyDtMM8th40kkVuVaINf6WUSQ_meuhSdHqs",
  "authDomain": "taskassign-4d8a7.firebaseapp.com",
  "databaseURL": "https://taskmanagement-aed46-default-rtdb.firebaseio.com",
 " projectId": "taskassign-4d8a7",
  "storageBucket": "taskassign-4d8a7.appspot.com",
  "messagingSenderId": "868821864936",
  "appId": "1:868821864936:web:0584e51e3cb3c4c9cc145d",
  
}
firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()





# Create your views here.
