from django.shortcuts import render
from Tollywood.forms import UserForm,Tollywoodform
from django.http import HttpResponse 
from django.contrib.auth.decorators import login_required
from Tollywood.models import Tollywood
# Create your views here.
def signup(request):
	if request.method=="POST":
		data=UserForm(request.POST)
		if data.is_valid():
			data.save()
			return HttpResponse("Done")
	form=UserForm()
	return render(request,'Tollywood/signup.html',{'form':form})
def home(request):
	return render(request,'Tollywood/home.html')
@login_required
def profile(request):
	return render(request,'Tollywood/profile.html')
@login_required
def addmovie(request):
	if request.method=="POST":
		data=Tollywoodform(request.POST,request.FILES)
		if data.is_valid():
			data.save()
			return HttpResponse("Uploaded data..!!!")
	form=Tollywoodform()
	return render(request,'Tollywood/addmovie.html',{'form':form})
def Tollywoodmovies(request):
	data=Tollywood.objects.all()
	return render(request,'Tollywood/Tollywoodmovies.html',{'data':data})
