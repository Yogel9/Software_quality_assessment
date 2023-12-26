from django.shortcuts import render


def index(request):
    """ Страница с метрикой Мартина"""
    context = {"title": 'Мартин'}
    return render(request, 'martin.html', {'context': context, })
