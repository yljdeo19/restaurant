from django.contrib.auth.forms import UserCreationForm
from accounts.models import account
from django import forms


class UserProfileForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control mb-4', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control mb-4', 'placeholder': 'Confirm Password'}))
    account_img = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control mb-4', 'id': 'acc'}))

    class Meta:
        model = account
        fields = ('username', 'first_name', 'last_name', 'account_img', 'password1', 'password2')
        widgets = {
            "username": forms.TextInput(
                attrs={'placeholder': 'Username', 'class': 'form-control mb-4'}),
            "first_name": forms.TextInput(
                attrs={'placeholder': 'First Name', 'class': 'form-control mb-4'}),
            "last_name": forms.TextInput(
                attrs={'placeholder': 'Last Name', 'class': 'form-control mb-4'}),

        }


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = account
        fields = ('username', 'first_name', 'last_name', 'account_img')


class ContactForm(forms.Form):
    contact_name = forms.CharField(max_length=500, widget=forms.TextInput(attrs={'id': 'name', 'class': 'form-control'}))
    contact_email = forms.EmailField(max_length=500, widget=forms.EmailInput(attrs={'id': 'email', 'class': 'form-control'}))
    content = forms.CharField(label='', widget=forms.Textarea(attrs={'id': 'message', 'class': 'form-control md-textarea', 'rows': '3'}))