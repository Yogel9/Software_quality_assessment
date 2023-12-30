from django.shortcuts import render

from halstead.models import HalsteadParam


def index(request):
    """ Страница с методом Холстеда"""
    context = {"title": 'Холстед',
               "my_param": HalsteadParam.objects.all(),}
    if request.method == 'POST':
        HalsteadParam.objects.create(n1=int(request.POST['Число простых операторов n1']),
                                     n2=int(request.POST['Число простых операндов n2']),
                                     hn1=int(request.POST['Общее число всех операторов N1']),
                                     hn2=int(request.POST['Общее число всех операндов N2']),
                                     k=int(request.POST['Входные/выходные переменные k']),)

    return render(request, 'halstead.html', {'context': context, })

