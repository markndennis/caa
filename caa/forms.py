from django import forms

class LoginForm(forms.Form):
    first_name = forms.CharField(label='First Name',max_length=40)
    last_name = forms.CharField(label='Last Name', max_length=40)
    password = forms.CharField(label='Password', max_length=40)
    