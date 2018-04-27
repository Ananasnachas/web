# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings

from questions.models import Question


class Answer(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='answers', verbose_name=u'Автор')
    question = models.ForeignKey(Question, related_name=u'answers', verbose_name=u'Вопрос')
    is_archive = models.BooleanField(default=False, verbose_name=u'Ответ в архиве')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    text = models.TextField(verbose_name=u'Содержимое Ответа', null=True)

    class Meta:
        verbose_name = u'Ответ'
        verbose_name_plural = u'Ответы'

    def __str__(self):
        return self.text