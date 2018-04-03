# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render


class Login(LoginView):

    template_name = 'users/login.html'


class Logout(LogoutView):

    template_name = 'users/logout.html'


def profile(request):

    return render(request, 'users/profile.html', {})