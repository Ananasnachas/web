# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name=u'Имя тега')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_archive = models.BooleanField(default=False, verbose_name=u'Тег в архиве')

    class Meta:
        verbose_name = u'Тег'
        verbose_name_plural = u'Теги'
        ordering = 'name', 'id'

    def __unicode__(self):
        return self.name
