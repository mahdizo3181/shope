from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class UserCreateForm(forms.ModelForm):
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'phone']

    def clean_password2(self):
        clean_data = self.cleaned_data
        if clean_data['password1'] and clean_data['password2'] and clean_data['password1'] != clean_data['password2']:
            raise forms.ValidationError('password must mach')
        return clean_data['password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password2'])
        if commit:
            user.save()
        return user


class UserChangedForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        help_text='you can change password using <a href=\'../password/\'>this is form<\a>.')

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'phone', 'password', 'last_login']

    def clean_password(self):
        return self.initial['password']


class UserRegistrForm(forms.Form):
    fullname = forms.CharField(label='',
                               widget=forms.TextInput(attrs={'class': 'text', 'placeholder': _('نام و نام خانوادگی')}))
    email = forms.EmailField(label='',
                             widget=forms.TextInput(attrs={'class': 'text text-left', 'placeholder': _('ایمیل')}))
    phone = forms.CharField(label='',
                            widget=forms.TextInput(attrs={'class': 'text text-left', 'placeholder': _('تلفن')}))
    password = forms.CharField(label='',
                               widget=forms.PasswordInput(
                                   attrs={'class': 'text text-left', 'placeholder': _('رمز عبور')}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={'class': 'text text-left', 'placeholder': _('تکرار رمز عبور')}))

    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email).exists()
        if user:
            raise ValidationError('this email already exists')
        return email

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        user = User.objects.filter(phone=phone).exists()
        if user:
            raise ValidationError('this phone already exists')
        return phone


class VerifyCodeForm(forms.Form):
    code = forms.IntegerField(label='', widget=forms.TextInput(
        attrs={'class': 'text text-left', 'placeholder': _('کد فعال سازی')}))


class UserLoginForm(forms.Form):
    email = forms.EmailField(label='',
                             widget=forms.TextInput(attrs={'class': 'text text-left', 'placeholder': _('ایمیل')}))
    password = forms.CharField(label='',
                               widget=forms.PasswordInput(
                                   attrs={'class': 'text text-left', 'placeholder': _('رمز عبور')}))
