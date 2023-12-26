from django.shortcuts import render

from halstead.models import Halstead


def index(request):
    """ Страница с методом Холстеда"""
    context = {"title": 'Холстед'}
    if request.method == 'POST':
        Halstead.objects.all().delete()
        Halstead.objects.create(request.POST['Число простых (уникальный) операторов n1'],
                                request.POST['Число простых (уникальный) операндов n2'],
                                request.POST['Общее число всех операторов N1'],
                                request.POST['Общее число всех операндов N2'],
                                request.POST['Входные/выходные переменные k'],)

    return render(request, 'halstead.html', {'context': context, })

