from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=200)
    profession = models.CharField(max_length=200)
    birth_year = models.PositiveSmallIntegerField()
    active = models.BooleanField(default=True)

    class Meta:
        db_table = "Student"

    def __str__(self):
        return int(self.id) + ' - ' + self.name
