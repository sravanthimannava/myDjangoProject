from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_page(_):
    return HttpResponse("Hello, This is Home")

def start_page(_):
    return HttpResponse("Hey You are just starting")

def last_page(_):
    return HttpResponse("Bye")

def index(request):
    dict_1={'Vaccine':['Covishield','Covaxin']}
    return render(request,'myFirstApp/index.html',context=dict_1)
