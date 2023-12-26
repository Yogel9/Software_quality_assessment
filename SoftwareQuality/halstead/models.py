from django.db import models


class Halstead(models.Model):
    n1 = models.FloatField()
    n2 = models.FloatField()
    bn1 = models.FloatField()
    bn2 = models.FloatField()
    k = models.FloatField()

