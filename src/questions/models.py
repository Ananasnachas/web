# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

from application import settings
from tags.models import Tag


class Question(models.Model):
    tags = models.ManyToManyField(Tag, related_name='questions', blank=True, verbose_name=u'Теги')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='questions', blank=True, null=True,
                               verbose_name=u'Автор')
    name = models.CharField(max_length=255, verbose_name=u'Имя вопроса')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_archive = models.BooleanField(default=False, verbose_name=u'Вопрос в архиве')

    class Meta:
        verbose_name = u'Вопрос'
        verbose_name_plural = u'Вопросы'
        ordering = 'name', 'id'

    def __unicode__(self):
        return self.name
