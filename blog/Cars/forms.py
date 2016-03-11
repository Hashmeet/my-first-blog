from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Post,SignUp

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text','image')

class SignForm(forms.ModelForm):

	class Meta:
		model = SignUp
		fields = ('name','email_id')

class MyRegistrationForm(UserCreationForm):
	email=forms.EmailField(required='True')

	class Meta:
		model=User
		fields=('username','email','password1','password2')	
	def save(self,commit=True):
		 	user=super(UserCreationForm,commit=False) 
		 	user.email=self.cleaned_data['email']
		 	if commit:
		 		user.save()
		 	return user	


			




