from django.db import models


class Actor(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=255)
    site = models.URLField(blank=True, null=True)
    email = models.EmailField()

    class Meta:
        db_table = 'actor'

    def __str__(self):
        return self.name + ' - ' + self.email
