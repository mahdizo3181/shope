from django.shortcuts import render, redirect
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework import authentication, generics, permissions, status
from rest_framework.views import APIView
from .forms import UserRegistrForm, VerifyCodeForm, UserLoginForm
import random
from utils import send_otp_code
from .models import OtpCode, User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.utils.translation import gettext as _
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator


# Create your views here.


class UserRegistrView(View):
    form_class = UserRegistrForm

    def get(self, request):
        form = self.form_class

        return render(request, 'accounts/register.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            random_code = random.randint(1000, 9999)
            send_otp_code(form.cleaned_data['phone'], random_code)
            OtpCode.objects.create(phone_number=form.cleaned_data['phone'], code=random_code)
            request.session['user_registration_info'] = {
                'phone_number': form.cleaned_data['phone'],
                'email': form.cleaned_data['email'],
                'username': form.cleaned_data['username'],
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'password': form.cleaned_data['password'],
            }
            messages.success(request, '.کد ۴ رقمی برای شما ارسال گردید', 'success')
            return redirect('accounts:verify_code')
        return render(request, 'accounts/register.html', {'form': form})


# @method_decorator(csrf_exempt, name='dispatch')
class UserRegistrVerifyCodeView(View):
    form_class = VerifyCodeForm

    def get(self, request):
        form = self.form_class
        return render(request, 'accounts/verify.html', {'form': form})

    def post(self, request):
        user_session = request.session['user_registration_info']
        code_instance = OtpCode.objects.get(phone_number=user_session['phone_number'])
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if cd['code'] == code_instance.code:
                User.objects.create_user(email=user_session['email'], username=user_session['username'],
                                         first_name=user_session['first_name'],
                                         last_name=user_session['last_name'], password=user_session['password'],
                                         phone=user_session['phone_number']
                                         )
                code_instance.delete()
                messages.success(request, '.ثبت نام با موفقیت انجام شد', 'success')
                return redirect('home:home')
            else:
                messages.error(request, '.کد وارد شده اشتباه است', 'danger')
                return redirect('accounts:verify_code')
        return redirect('home:home')


class UserLogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.success(request, '.با موفقیت خارج شدید ', 'success')
        return redirect('home:home')


class UserLoginView(View):
    form_class = UserLoginForm
    template_name = 'accounts/login.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, '.با موفقیت وارد شدید', 'success')
                return redirect('home:home')
            messages.error(request, '.نام کاربری یا رمز عبور اشتباه است', 'warning')
        return render(request, self.template_name, {'form': form})
