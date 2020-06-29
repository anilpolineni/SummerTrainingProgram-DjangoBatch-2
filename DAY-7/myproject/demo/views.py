from django.shortcuts import render
import datetime

def time(request):
    date_time = datetime.datetime.now()
    return render(request,'time.html',{'data':date_time})


def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        phno = request.POST['phone']
        mail = request.POST['mail']
        return render(request,'details.html',{'name':name,'phno':phno,'mail':mail})
    return render(request, 'register.html')