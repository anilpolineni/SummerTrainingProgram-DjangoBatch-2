from django.shortcuts import render
from Tollywood.forms import UserForm
from django.http import HttpResponse 
from django.contrib.auth.decorators import login_required
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
	data={'name':"vijay","empid":426,"salary":"30k",'age':26}
	return render(request,'Tollywood/home.html',{"data":data})
@login_required
def addmovie(request)