from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=255)
    site = models.URLField(blank=True, null=True)
    email = models.EmailField()

    class Meta:
        db_table = 'authors'

    def __str__(self):
        return self.name + ' - ' + self.email


class Article(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    insert_date = models.DateField(auto_now=True)
    update_date = models.DateField(auto_now_add=True)
    text = models.TextField()

    class Meta:
        db_table = 'articles'

    def __str__(self):
        return self.title
