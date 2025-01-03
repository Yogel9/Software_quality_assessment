from django.db import models


class ChepinParam(models.Model):
    param1 = models.IntegerField(
        verbose_name="Вводимые переменные для расчетов и для обеспечения вывода"  # noqa E501
    )
    param2 = models.IntegerField(verbose_name="Весовой коэффициент 1")
    param3 = models.IntegerField(
        verbose_name="Модифицируемые, или создаваемые  внутри программы переменные"  # noqa E501
    )
    param4 = models.IntegerField(verbose_name="Весовой коэффициент 2")
    param5 = models.IntegerField(
        verbose_name="Переменные, участвующие в управлении"
        " работой программного модуля"
    )
    param6 = models.IntegerField(verbose_name="Весовой коэффициент 3")
    param7 = models.IntegerField(
        verbose_name="Не используемые в программе («паразитные») переменные"  # noqa E501
    )
    param8 = models.IntegerField(verbose_name="Весовой коэффициент 4")
