from django.shortcuts import render,redirect

from courses.forms import CourseForm

from.models import Course

from django.http import HttpResponse

from django.contrib import messages

# Create your views here.

def home(request):
	return render(request,'courses/index.html')



def addcourse(request):
	if request.method=="POST":
		form=CourseForm(request.POST)
		if form.is_valid():
			form.save()
			course_name=form.cleaned_data.get('course_name')
			# return HttpResponse('%s course is successfully added..!'%(course_name))
			messages.success(request, '%s course is successfully added..!'%(course_name))
			return redirect('showcourses')

	form=CourseForm()
	return render(request,'courses/addcourse.html',{"form":form})



def showcourses(request):
	courses=Course.objects.all()
	return render(request,'courses/showcourses.html',{'courses':courses})


def courseedit(request,id):
	data=Course.objects.get(id=id)
	if request.method=="POST":
		form=CourseForm(request.POST,instance=data)
		if form.is_valid():
			form.save()
			course_name=form.cleaned_data.get('course_name')
			# return HttpResponse('%s course is successfully updated'%(course_name))
			messages.warning(request,'%s course is successfully updated'%(course_name))
			return redirect('showcourses')
	form=CourseForm(instance=data)
	context={
	'data':data,
	'form':form
	}
	return render(request,'courses/courseedit.html',context)




def coursedelete(request,id):
	data=Course.objects.get(id=id)
	# if request.method=="POST":
	# 	data.delete()
	# 	return redirect('showcourses')
	# return render(request,'courses/coursedelete.html',{})
	data.delete()
	return redirect('showcourses')



