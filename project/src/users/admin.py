# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as OldUserAdmin
from users.models import User


@admin.register(User)
class UserAdmin(OldUserAdmin):
    list_display = 'username', 'created'
    search_fields = 'username', 'questions__name'
