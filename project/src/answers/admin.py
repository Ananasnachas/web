# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from answers.models import Answer


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = 'id', 'author', 'question'
    search_fields = 'id', 'question'
