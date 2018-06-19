from django import forms
from AppTwo.models import User

class NewUserForm(forms.ModelForm):
    class Meta: # Omitting parenthesis is OK in Python3.
        model = User
        fields = '__all__'
