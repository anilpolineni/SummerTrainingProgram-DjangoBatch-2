from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def home(request):
	return HttpResponse('<h1 style=color:red;font-size:50px;>welcome to Django</h1>')


# passing static variables

def name(request):
	name='APSSDC'
	return HttpResponse('<h3 style=color:green>welcome To '+name+'</h3>')
 

def fullname(request):
	fname='sai'
	lname='kumar'
	return HttpResponse('<h2> My firstname is %s & My last Name is %s</h2>'%(fname,lname))

# passing Dynamic variables
def myname(request,name):
	return HttpResponse('<h2 style=color:meroon;> My Name is %s</h2>'%(name))


def details(request,name,rollno):
	return HttpResponse('<h3 style=color:blue> My name is %s & My Rollno is %s</h3>'%(name,rollno))