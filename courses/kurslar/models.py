from django.db import models
class Yonalish(models.Model):
    nom=models.CharField(choices=(("1"),("aniq"),("2"),("til"),("3"),("tabiat")))
    kod=models.SmallAutoField()
    boshlangan_sana=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.nom
class Oqituvchi(models.Model):
    ism=models.CharField(max_length=30)
    familiya = models.CharField(max_length=30)
    yosh = models.PositiveSmallIntegerField()
    def __str__(self):
        return f"{self.ism}{self.familiya}"
class Fan(models.Model):
    nom=models.CharField(max_length=30)
    yonalish=models.ManyToManyField(Yonalish)
    oqituvchilar=models.ManyToManyField(Oqituvchi)
    def __str__(self):
        return self.nom
