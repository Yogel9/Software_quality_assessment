from django.core.validators import MinValueValidator
from django.db import models


class HalsteadParam(models.Model):
    n1 = models.IntegerField(verbose_name='Уник. операторов', validators=[MinValueValidator(0)])
    n2 = models.IntegerField(verbose_name='Уник. операндов', validators=[MinValueValidator(0)])
    hn1 = models.IntegerField(verbose_name='Общ. операторов', validators=[MinValueValidator(0)])
    hn2 = models.IntegerField(verbose_name='Общ. операндов', validators=[MinValueValidator(0)])
    k = models.IntegerField(verbose_name='Входные/выходные переменные', validators=[MinValueValidator(0)])

