from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)
