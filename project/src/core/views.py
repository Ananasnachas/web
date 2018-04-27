# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import Sum
from django.shortcuts import render, HttpResponse, get_object_or_404

from questions.models import Question



def main_page(request):
    user = request.user
    questions = Question.objects.all().filter(is_archive=False)
    questions = questions.annotate(total_likes=Sum('likes')).order_by('-total_likes')[:10]
    return render(request, 'core/main_page.html', {'questions':questions, 'user':user,})
