from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime


class Student(models.Model):
    name = models.CharField(max_length=200)
    profession = models.CharField(max_length=200)
    birth_year = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1900), 
        MaxValueValidator(datetime.now().year)])
    active = models.BooleanField(default=True)

    class Meta:
        db_table = "students"

    def __str__(self):
        return str(self.id) + ' - ' + self.name
