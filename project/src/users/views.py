# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.hashers import check_password
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model, authenticate, update_session_auth_hash
from django.contrib.auth import login
from users.forms import RegistrationForm, UsersListForm

User = get_user_model()


class Login(LoginView):
    template_name = 'users/login.html'


class Logout(LogoutView):
    template_name = 'users/logout.html'

def password_edit(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('my_profile')
        else:
            messages.error(request, 'Исправьте ошибки!')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'users/password_edit.html', {
        'form': form
    })


def registration(request):
    if request.method == 'GET':
        form = RegistrationForm()
        return render(request, 'users/registration.html', {'form': form})
    elif request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('my_profile')
        else:
            return render(request, 'users/registration.html', {'form': form, 'text': 'Try again'})


def my_profile(request):
    user = request.user
    context = {
        'user': user,
    }
    return render(request, 'users/my_profile.html', context)


def profile(request, id):
    user = get_object_or_404(User, id=id)
    name = ''
    if user.is_superuser:
        name = 'Admin'
    context = {
        'user': user,
        'name': name
    }
    return render(request, 'users/profile.html', context)


def users_list(request):
    users = User.objects.all().filter(is_archive=False, is_superuser=False)
    form = UsersListForm(request.GET)
    if form.is_valid():
        input = form.cleaned_data
        if input['sort']:
            sort = input['sort']
            users = users.order_by(sort)
        if input['search']:
            users = users.filter(first_name__icontains=input['search'])
    context = {
        'users': users,
        'form': form,
    }
    return render(request, 'users/users_list.html', context)