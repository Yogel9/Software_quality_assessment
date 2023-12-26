from django.db import models
from django.core.validators import MinValueValidator

class HolstedParam(models.Model):
    n1 = models.IntegerField(name='Уник. операторов', validators=[MinValueValidator(0)])
    n2 = models.IntegerField(name='Уник. операндов', validators=[MinValueValidator(0)])
    hn1 = models.IntegerField(name='Общ. операторов', validators=[MinValueValidator(0)])
    hn2 = models.IntegerField(name='Общ. операндов', validators=[MinValueValidator(0)])
    k = models.IntegerField(name='Входные/выходные переменные', validators=[MinValueValidator(0)])

