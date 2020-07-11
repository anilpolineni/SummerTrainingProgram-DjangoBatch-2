from django.shortcuts import render
from mailsending.settings import EMAIL_HOST_USER #
from django.core.mail import send_mail
from django.http import HttpResponse
from django.core.mail import EmailMessage
# from mailsending import settings 
# Create your views here.
def mail(req):
	if req.method =="POST":
		sub="Reg Testing mail"
		tomail=req.POST['mail']
		msg=req.POST['msg']
		frommail=EMAIL_HOST_USER
		# frommail=settings.EMAIL_HOST_USER
		print(tomail,msg,frommail)
		send_mail(sub,msg,frommail,[tomail])
		return HttpResponse("Mail Send Sucessfully....!!!!")
	return render(req,'app1/mail.html')
def attach(req):
	if req.method=="POST":
		sub=req.POST['sub']
		msg=req.POST['msg']
		mailid=req.POST['email']
		frommail=EMAIL_HOST_USER
		email=EmailMessage(sub,msg,EMAIL_HOST_USER,[mailid])
		email.content_subtype='html'
		file=req.FILES['file']
		email.attach(file.name,file.read(),file.content_type)
		email.send()
		return HttpResponse("Done")
	return render(req,'app1/attach.html')
def hello():
	return HttpResponse("hello")