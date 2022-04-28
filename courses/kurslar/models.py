from django.db import models


class Fan(models.Model):
    nom = models.CharField(max_length=30)
    code = models.PositiveSmallIntegerField(default=0)
    start_date = models.DateField(default="2007-03-12")
    is_active = models.BooleanField(default=True)


class Ustoz(models.Model):
    ism = models.CharField(max_length=30)


class Yonalish(models.Model):
    nom = models.CharField(max_length=30)
    fanlar = models.ManyToManyField(Fan)
    ustozlar = models.ManyToManyField(Ustoz)