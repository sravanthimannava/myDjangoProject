from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection

cursor = connection.cursor()
cursor.execute('''SELECT USER FROM user_list''')
row = cursor.fetchall()

def db_connection_fetch(connection,query):
    with connection.cursor() as c :
        c.execute(query)
        rows = c.fetchone()
    return rows

def home_page(_):
    password='RK12'
    query='''select password from user_list where user= 'Roheeth' '''
    val,=db_connection_fetch(connection,query)
    if val == password:
        return render(_,'myFirstApp/index.html')
    else:
        return HttpResponse("Invalid Credentials")

def start_page(_):
    return HttpResponse("Hey You are just starting")

def last_page(_):
    return HttpResponse("Bye")

def index(request):
    dict_1={'Numbers':"One\nTwo\nThree"}
    return render(request,'myFirstApp/index.html',context=dict_1)
