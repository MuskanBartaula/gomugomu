# from django import forms
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import (Layout, Field, Div)
# from django.contrib.auth.forms import UserCreationForm
# from .models import User


# class SignupForm(UserCreationForm):
#     first_name = forms.CharField(
#         widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control'}),
#         label='',
#         required=False,
#     )
#     last_name = forms.CharField(
#         widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control'}),
#         label='',
#         required=False,
#     )
#     email = forms.CharField(
#         widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'}),
#         label='',
#         required=False,
#     )
#     password1 = forms.CharField(
#         widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}),
#         label='',
#         required=False,
#     )
#     password2 = forms.CharField(
#         widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'form-control'}),
#         label='',
#         required=False,
#     )

#     form_layout = Layout(Div(
#         Field('first_name', wrapper_class='form-group'),
#         Field('last_name', wrapper_class='form-group'),
#         Field('email', wrapper_class='form-group'),
#         Field('password1', wrapper_class='form-group'),
#         Field('password2', wrapper_class='form-group'),
#     ))

#     class Meta:
#         model = User
#         fields = ["first_name", "last_name", "email", "password1", "password2"]

#     def __init__(self, *args, **kwargs):
#         super(SignupForm, self).__init__(*args, **kwargs)
#         self.helper = FormHelper(self)
#         self.helper.layout = Layout(
#             self.form_layout
#         )

#     def clean_email(self):
#         """
#        Validate that the supplied email address is unique for the
#        site.

#        """
#         if not self.cleaned_data['email']:
#             raise forms.ValidationError("This email address is already in use. Please supply a different email address.")
#         return self.cleaned_data['email']
