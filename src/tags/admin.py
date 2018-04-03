# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from tags.models import Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):

    list_display = 'name', 'created'
    search_fields = 'name','questions__name'
