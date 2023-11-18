from django.db import models

class CarMark(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'{self.name}'

class CarModel(models.Model):
    name = models.CharField(max_length=100)
    carmark = models.ForeignKey(CarMark, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.name}'