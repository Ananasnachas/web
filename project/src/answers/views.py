# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, UpdateView

from answers.models import Answer


class AnswerEdit(UpdateView):
    model = Answer
    fields = 'text',
    context_object_name = 'answer'
    template_name = 'answers/answer_edit.html'

    def get_success_url(self):
        return reverse('question_detail', kwargs={'id': self.object.question.id})


class AnswerCreate(CreateView):
    model = Answer
    fields = 'text',
    context_object_name = 'answer'
    template_name = 'answers/answer_create.html'

    def get_success_url(self):
        return reverse('question_detail', kwargs={'id': self.object.question.id})


def answer_detail(request, id):
    answer = get_object_or_404(Answer, id=id)
    name = ''
    if answer.author.is_superuser:
        name = 'Admin'
    context = {
        'answer': answer,
        'name': name
    }
    return render(request, 'answers/answer_detail.html', context)
