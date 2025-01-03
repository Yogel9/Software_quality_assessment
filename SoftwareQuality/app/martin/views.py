from django.shortcuts import render

from .models import MartinParam


def index(request):
    """ Страница с метрикой Мартина"""
    context = {"title": 'Мартин',
               'my_param': MartinParam.objects.all()}

    if request.method == 'POST':
        MartinParam.objects.create(param1=int(request.POST['Са (центростремительное сцепление)']),
                                   param2=int(request.POST['Се (центробежное сцепление)']),
                                   param3=int(request.POST['nA количество абстрактных классов в категории']),
                                   param4=int(request.POST['nАll общее количество классов в категории']),)


    return render(request, 'martin.html', {'context': context, })
