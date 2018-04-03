# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from tags.models import Tag


def tag_detail(request, id):
    tags = get_object_or_404(Tag,id=id)
    context = {
        'tag': tags
    }
    return render(request, 'tags/tag_detail.html', context)


def tags_list(request):
    context = {
        'tags': Tag.objects.all().filter(is_archive=False)
    }
    return render(request,'tags/list.html',context)