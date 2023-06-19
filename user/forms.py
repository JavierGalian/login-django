from django import forms
from .models import User

class CreateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email', 'password','image']