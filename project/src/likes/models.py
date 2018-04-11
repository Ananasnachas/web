# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from answers.models import Answer
from questions.models import Question
from users.models import User


class Like(models.Model):
    author = models.ForeignKey(User, related_name='likes', verbose_name=u'Автор', )
    created = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question, related_name='likes', verbose_name=u'Вопрос', null=True)
    answer = models.ForeignKey(Answer, related_name='likes', verbose_name=u'Ответ', null=True)

    def __unicode__(self):
        return self.id
