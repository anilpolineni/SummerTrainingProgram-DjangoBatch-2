from django.forms import ModelForm # from django import forms

from courses.models import Course




class CourseForm(ModelForm):

	class Meta():

		model=Course

		fields='__all__' # ['couse_name','description']



