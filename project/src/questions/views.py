# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect

from likes.models import Like
from questions.forms import QuestionForm, QuestionsListForm
from tags.models import Tag
from tags.views import make_new_tag
from .models import Question


def question_detail(request, id):
    question = get_object_or_404(Question, id=id)
    name = ''
    if question.author.is_superuser:
        name = 'Admin'
    user = request.user
    if request.method == 'POST' and user.id is not None:
        question_likes = question.likes.all().filter(author__id=user.id)
        if question_likes.all().count() == 0:
            like = Like(author=user, question=question)
            like.save()
        else:
            for l in question_likes:
                l.delete()
    context = {
        'question': question,
        'name': name,
        'likes': question.likes.all().count(),
        'user': user,
    }
    return render(request, 'questions/question.html', context)


def questions_list(request):
    questions = Question.objects.all().filter(is_archive=False)
    form = QuestionsListForm(request.GET)
    if form.is_valid():
        input = form.cleaned_data

        if input['sort']:
            sort = input['sort']
            questions = questions.order_by(sort)
        if input['search']:
            questions = questions.filter(name__icontains=input['search'])
    context = {
        'questions': questions,
        'form': form,
    }
    return render(request,'questions/questions_list.html',context)


def question_create(request):
    if request.method == 'GET':
        form = QuestionForm()
        return render(request, 'questions/question_create.html', {'form': form})
    elif request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            text = form.cleaned_data['text']
            tags = form.cleaned_data['tags']
            author = request.user
            question = Question(name=name, text=text, author=author)
            question.save()
            splited_tags = tags.split(u'@@', -1)
            for tag_name in splited_tags:
                is_tag_new = True
                for tag in Tag.objects.all():
                    if tag.name == tag_name:
                        question.tags.add(tag)
                        is_tag_new = False
                        break
                if is_tag_new:
                    question.tags.add(make_new_tag(tag_name))
                question.save()
            return redirect('question_detail', id=question.id)
        else:
            return render(request, 'questions/question_create.html', {'form': form})


def question_edit(request, id=None):
    question = get_object_or_404(Question, id=id)
    tags = ''
    for tag in question.tags.all():
        tags += tag.name
        tags += '@@'
    if request.method == 'GET':
        form = QuestionForm(initial={'name': question.name, 'text': question.text, 'tags': tags})
        return render(request, 'questions/question_edit.html', {'form': form})
    elif request.method == 'POST':
        form = QuestionForm(request.POST, initial={'name': question.name, 'text': question.text, 'tags': tags})
        if form.is_valid():
            name = form.cleaned_data['name']
            text = form.cleaned_data['text']
            tags = form.cleaned_data['tags']
            question.name = name
            question.text = text
            question.save()
            splited_tags = tags.split(u'@@', -1)
            question.tags.clear()
            for tag_name in splited_tags:
                if tag_name is not '':
                    is_tag_new = True
                    for tag in Tag.objects.all():
                        if tag.name == tag_name:
                            question.tags.add(tag)
                            is_tag_new = False
                            break
                    if is_tag_new:
                        question.tags.add(make_new_tag(tag_name))
                    question.save()
            for tag in Tag.objects.all():
                if tag.questions.count() is 0:
                    tag.delete()
            return redirect('question_detail', id=question.id)
        else:
            return render(request, 'questions/question_edit.html', {'form': form})
