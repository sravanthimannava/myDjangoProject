from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection

# Create your views here.

cursor = connection.cursor()
cursor.execute('''SELECT USER FROM user_list''')
row = cursor.fetchall()

def db_connection_fetch(connection,query):
    with connection.cursor() as c :
        c.execute(query)
        row = c.fetchone()
    return row

def home_page(_):
    uname='Roheeth'
    passs='RK123'
    query='SELECT True FROM User_list WHERE user ="' + uname + '" AND password ="' + passs + '"'
    val,=db_connection_fetch(connection,query)
    if val == 1:
        return render(_,'myFirstApp/index.html')
    else:
        return HttpResponse(val)

def start_page(_):
    return HttpResponse("Hey You are just starting")

def last_page(_):
    return HttpResponse("Bye")

def index(request):
    dict_1={'Numbers':"One\nTwo\nThree"}
    return render(request,'myFirstApp/index.html',context=dict_1)
