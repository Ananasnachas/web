# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404

from tags.forms import TagsListForm
from tags.models import Tag


def tag_detail(request, id):
    tag = get_object_or_404(Tag, id=id)
    context = {
        'tag': tag
    }
    return render(request, 'tags/tag_detail.html', context)


def tags_list(request):
    tags = Tag.objects.all().filter(is_archive=False)
    form = TagsListForm(request.GET)
    if form.is_valid():
        input = form.cleaned_data
        if input['sort']:
            sort = input['sort']
            tags = tags.order_by(sort)
        if input['search']:
            tags = tags.filter(name__icontains=input['search'])
    context = {
        'tags': tags,
        'form': form,
    }
    return render(request,'tags/list.html',context)

def make_new_tag(name):
    tag = Tag(name=name)
    tag.save()
    return tag