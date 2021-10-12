
from django.contrib.auth import login, authenticate, get_user_model

from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, FormView, TemplateView
from django.contrib.auth import login as auth_login

from accounts import forms
from accounts.forms import UserRegistrationForm, SignForm

User = get_user_model()

class RegisterViews(CreateView):
    model = User
    template_name = 'pages/registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('success_registration')

class SuccessfulRegistrationView(TemplateView):
    template_name = 'pages/success_registration.html'

class ActivationView(View):
    def get(self, request):
        code = request.GET.get('u')
        if code:
            user = get_object_or_404(User, activation_code=code)
            user.is_active = True
            user.activation_code = ''
            user.save()
            return render(request, 'activation.html', {})
        else:
            return render(request, 'pages/sign.html', status=404)


class SignView(LoginView):
    template_name = 'pages/sign.html'
    form_class = SignForm
    success_url = reverse_lazy('home')




