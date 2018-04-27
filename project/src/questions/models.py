# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from tags.models import Tag
from users.models import User


class Question(models.Model):
    tags = models.ManyToManyField(Tag, related_name='questions', blank=True, verbose_name=u'Теги')
    author = models.ForeignKey(User, related_name='questions', blank=True, null=True,
                               verbose_name=u'Автор')
    name = models.CharField(max_length=255, verbose_name=u'Имя вопроса')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_archive = models.BooleanField(default=False, verbose_name=u'Вопрос в архиве')
    text = models.TextField(verbose_name=u'Текст ответа', null=True)

    class Meta:
        verbose_name = u'Вопрос'
        verbose_name_plural = u'Вопросы'
        ordering = 'name', 'id'

    def __unicode__(self):
        return self.name
