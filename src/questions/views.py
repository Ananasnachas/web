# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import Question


def question_detail(request, id):
    question = get_object_or_404(Question, id=id)
    context = {
        'question': question
    }
    return render(request, 'questions/question.html', context)


def questions_list(request):
    context = {
        'questions': Question.objects.all().filter(is_archive=False)
    }
    return render(request,'questions/questions_list.html',context)

