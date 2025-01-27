from django.db import models


class Tramite(models.Model):
    nombre = models.CharField(max_length=100)
    diasReport = models.IntegerField()

    def __str__(self):
        return f"Tramite: {self.nombre}"


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    # address = models.TextField()
    rif = models.IntegerField()

    def __str__(self):
        return f"Cliente: {self.name} - {self.rif}"


class Calendario(models.Model):
    year = models.IntegerField()
    mes = models.IntegerField()
    dias = models.JSONField()
    tramites = models.ForeignKey(Tramite, on_delete=models.CASCADE)

    #
    def __str__(self):
        return f"{self.year}-{self.mes}"
