# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import reverse
from django.views.generic import CreateView, UpdateView

from answers.models import Answer


class AnswerEdit(UpdateView):
    model = Answer
    fields = 'text',
    context_object_name = 'answer'
    template_name = 'answers/answer_edit.html'

    def get_queryset(self):
        queryset = super(AnswerEdit, self).get_queryset()
        queryset = queryset.filter(author=self.request.user, id=self.kwargs.get('id'))
        return queryset

    def get_success_url(self):
        return reverse('question_detail', kwargs={'id': Answer.objects.all().get(id=self.kwargs.get('id'))
                       .question_id})


class AnswerCreate(CreateView):
    model = Answer
    fields = 'text',
    context_object_name = 'answer'
    template_name = 'answers/answer_create.html'

    def form_valid(self, form):
        form.instance.question_id = self.kwargs.get('id')
        form.instance.author = self.request.user
        return super(AnswerCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('question_detail', kwargs={'id': self.kwargs.get('id')})