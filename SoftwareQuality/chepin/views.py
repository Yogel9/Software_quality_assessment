from django.shortcuts import render


def index(request):
    """ Страница с метрикой Чепина"""
    context = {"title": 'Чепин'}
    return render(request, 'chepin.html', {'context': context, })
