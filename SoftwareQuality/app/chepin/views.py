from django.shortcuts import render

from .models import ChepinParam


def index(request):
    """Страница с метрикой Чепина"""
    context = {
        "title": "Чепин",
        "my_param": ChepinParam.objects.all(),
    }
    if request.method == "POST":
        ChepinParam.objects.create(
            param1=int(request.POST["Вводимые переменные"]),
            param2=int(request.POST["Весовой коэффициент P"]),
            param3=int(request.POST["Модифицируемые переменные"]),
            param4=int(request.POST["Весовой коэффициент M"]),
            param5=int(request.POST["Переменные, уч. в управлении"]),
            param6=int(request.POST["Весовой коэффициент С"]),
            param7=int(request.POST["Не используемые переменные"]),
            param8=int(request.POST["Весовой коэффициент T"]),
        )

    return render(
        request,
        "chepin.html",
        {
            "context": context,
        },
    )
