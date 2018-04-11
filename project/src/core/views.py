# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, get_object_or_404


def main_page(request):
    return render(request, 'core/main_page.html', {})
