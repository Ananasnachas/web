# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-10 09:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0007_auto_20180403_1155'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='text',
            field=models.CharField(max_length=5000, null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043e\u0442\u0432\u0435\u0442\u0430'),
        ),
    ]
