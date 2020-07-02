from django.shortcuts import render, redirect
from .models import SignUp
from django.http import HttpResponse
from django.contrib import messages


def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        roll_num = request.POST.get('roll_num')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        person = SignUp(name=name,roll_num=roll_num,
                        email=email,age=age,gender=gender)
        person.save()
        messages.success(request,'Student added successfully :)')
        return redirect(display)
    return render(request,'student/signup.html')


def display(request):
    data = SignUp.objects.all()
    return render(request, 'student/display.html', {'data': data})


def edit(request,roll):
    data = SignUp.objects.get(roll_num=roll)
    if request.method == "POST":
        data.name = request.POST.get('name')
        data.roll_num = request.POST.get('roll_num')
        data.email = request.POST.get('email')
        data.age = request.POST.get('age')
        data.gender = request.POST.get('gender')
        data.save()
        messages.info(request,data.name+' Details updated successfully')
        return redirect(display)
    return render(request, 'student/edit.html',{'data': data})


def delete(request,roll):
    data = SignUp.objects.get(roll_num=roll)
    data.delete()
    return redirect(display)