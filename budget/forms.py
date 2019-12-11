from django import forms
from django.contrib.auth.models import User

from .models import Loan

class DateInput(forms.DateInput):
    input_type = 'date'

class LoanForm(forms.ModelForm):

    class Meta:
        model = Loan
        fields = ('name', 'begin_date', 'end_date', 'amount')
        widgets = {
            'begin_date': DateInput(),
            'end_date': DateInput(),
        }

class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)
    confirm = forms.CharField(max_length=20, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password', 'confirm')
