from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import *
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'box'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'box'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'box'}))
    password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'box'}))
    password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'box'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'box'
        self.fields['password1'].widget.attrs['class'] = 'box'
        self.fields['password2'].widget.attrs['class'] = 'box'
