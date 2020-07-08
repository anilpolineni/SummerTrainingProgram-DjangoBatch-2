from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from myapp.models import User_register
from django.forms import ModelForm

class User_form(UserCreationForm):
	class Meta:
		model=User
		fields=['username','first_name','last_name','password1','password2','email']#'__all__'

class User_login(UserCreationForm):
	class Meta:
		model=User
		fields=['username','password1']

class User_reg_form(ModelForm):
	class Meta:
		model=User_register
		fields=['name','mailid','phno']
class User_reg_login(ModelForm):
	class Meta:
		model=User_register
		fields=['username','password']
