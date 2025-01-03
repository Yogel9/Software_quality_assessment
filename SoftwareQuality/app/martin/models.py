from django.db import models


class MartinParam(models.Model):
    param1 = models.IntegerField(
        verbose_name="Са (центростремительное сцепление)"
    )  # noqa E501
    param2 = models.IntegerField(verbose_name="Се (центробежное сцепление)")
    param3 = models.IntegerField(
        verbose_name="nA количество абстрактных классов в категории"
    )
    param4 = models.IntegerField(
        verbose_name="nАll общее количество классов в категории"
    )
