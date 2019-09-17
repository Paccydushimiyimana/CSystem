from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    phone = forms.IntegerField()
    stdtype = forms.CharField(max_length=30, help_text='your type')
    regnumber = forms.IntegerField() 
    level = forms.IntegerField()
    school = forms.CharField(max_length=30, help_text='your school')
    department = forms.CharField(max_length=30, help_text='your department')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2', 'phone','stdtype','regnumber',
                    'level','school','department')
