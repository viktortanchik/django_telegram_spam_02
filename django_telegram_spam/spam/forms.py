from django import forms
from .models import *
#from .models import Image
from django.contrib.auth.models import User

class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        #exclude = ["texts","gender","contact","Main_Img","user"]
        exclude = [""]

        #fields = ['__all__']
        widgets = {
            'gender': forms.RadioSelect(),

        }
        #'hotel_Main_Img':forms.ImageField()


class SubscriberForm_test(forms.ModelForm):
    class Meta:
        model = User_settings
        exclude = [""]


###########################  USERS   ######################
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)



class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

