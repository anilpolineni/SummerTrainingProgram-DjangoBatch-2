from django.contrib import admin
from django.urls import path,include
from demo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('time/',views.time, name= 'time'),
    path('register/',views.register, name='register'),
    path('student/',include('stundent.urls')),
]
