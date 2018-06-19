from django import forms
from django.core import validators

def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("Name needs to start with z")

class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_z])
    email = forms.EmailField()
    verifyemail = forms.EmailField(label='Enter your email again:')
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        """"clean is used to clean the entire form at once"""
        all_clean_data = super().clean() # super.clean() returns all form data
        email = all_clean_data['email']
        vmail = all_clean_data['verifyemail']
        if email != vmail:
            raise forms.ValidationError("Make sure emails match!")

    # Django built-in form validation
    # botcatcher = forms.CharField(required=False, widget=forms.HiddenInput,
    #                              validators=[validators.MaxLengthValidator(0)])
    # Manual form validation
    # `required = False` because this field will not appear on the page.
    # botcatcher = forms.CharField(required=False, widget=forms.HiddenInput)
    #
    # def clean_botcatcher(self):
    #     """Django looks for methods in `forms.Form` that start with 'clean_'
    #        and looks for fields named the substring after '_'."""
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError("GOTCHA BOT!")
    #     return botcatcher
