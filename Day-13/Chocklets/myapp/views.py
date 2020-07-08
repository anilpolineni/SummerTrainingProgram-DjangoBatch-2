from django.shortcuts import render,redirect
from myapp.forms import User_form,User_login,User_reg_form,User_reg_login
from django.http import HttpResponse
from django.contrib.auth.models import User
from myapp.models import User_register
from django.core.mail import send_mail
from Chocklets.settings import EMAIL_HOST_USER


def register(request):
	if request.method=="POST":
		data=User_reg_form(request.POST)
		data.save()
		myinfo=User_register.objects.get(name=request.POST['name'])
		myinfo.username=myinfo.name+"_apssdc"
		psw=myinfo.name[:2]+"@#"+myinfo.phno[-2:]	
		myinfo.password=psw
		myinfo.save()
		sub="Reg User Credintials "
		msg="Welcome to Our New Chocklets if your want to loin go through below Credintials"+"User Name is --->"+myinfo.name+"_apssdc"+" Password is --->"+psw
		sender=EMAIL_HOST_USER
		reciver=myinfo.mailid
		send_mail(sub,msg,sender,[reciver])
		return HttpResponse("If You want to login our Portal can you please check your maild for your Credintials")
	form=User_reg_form()
	return render(request,'myapp/register.html',{'form':form})

def login(request):
	if request.method=="POST":
		username=request.POST['username']
		password=request.POST['password']
		data=User_register.objects.get(username=username,password=password)
		if data:
			return render(request,'myapp/home.html',{'data':data.username})
	form=User_reg_login()
	return render(request,'myapp/login.html',{'form':form})
def changepassword(request,name):
	if request.method=="POST":
		password1=request.POST['password1']
		password2=request.POST['password2']
		password3=request.POST['password3']
		data=User_register.objects.get(username=name,password=password1)
		if data:
			if password2==password3:
				data.password=password3
				data.save()
				return render(request,'myapp/home.html',{'data':name})
			else:
				return HttpResponse("Dos't match conf and new password...!!!")
		else:
			return HttpResponse("Invalid...!!")
	# data=User_register.objects.get(username=name)
	return render(request,'myapp/changepassword.html',{'name':name})

def forgotpassword(request):
	if request.method=="POST":
		data=User_register.objects.get(mailid=request.POST['email'])
		sub="Reg User Password "
		msg="username is "+"'"+data.username +"'"+" your Password is  "+"'"+data.password+"'"
		sender=EMAIL_HOST_USER
		reciver=request.POST['email']
		send_mail(sub,msg,sender,[reciver])
		return redirect('/login')
	return render(request,'myapp/forgotpassword.html')
# Create your views here.
# def register(request):
# 	if request.method=="POST":
# 		data=User_form(request.POST)
# 		if data.is_valid():
# 			data.save()
# 			return HttpResponse("Done")
# 	form=User_form()
# 	return render(request,'myapp/register.html',{'form':form})


# def login(request):
# 	if request.method=="POST":
# 		print(request.POST['username'],request.POST['password1'])
# 		data=User.objects.filter(username=request.POST['username'],password1=request.POST['password1'])
# 		print(data.username)
# 		print(data.password1)
# 		if data:
# 			return HttpResponse("Welcome to"+request.POST['username'])
# 		else:
# 			return HttpResponse("login Failed")
# 	form=User_login()
# 	return render(request,'myapp/login.html',{'form':form})
