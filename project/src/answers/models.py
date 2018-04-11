# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from questions.models import Question
from users.models import User


class Answer(models.Model):
    author = models.ForeignKey(User, related_name='answers', verbose_name=u'Автор')
    created = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question, related_name='answers', verbose_name=u'Вопрос')
    text = models.TextField(max_length=5000, verbose_name=u'Текст ответа')
    is_archive = models.BooleanField(default=False, verbose_name=u'Ответ в архиве')

    def __unicode__(self):
        return self.id
