from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.signup, name='student_signup'),
    path('display', views.display, name='display'),
    path('edit/<str:roll>', views.edit, name='edit'),
    path('delete/<str:roll>', views.delete, name='delete')
]