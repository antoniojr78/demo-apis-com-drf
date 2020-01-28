from django.contrib import admin
from .models import Author, Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'insert_date', 'update_date')

    class Meta:
        model = Article


admin.site.register(Author)
admin.site.register(Article, ArticleAdmin)
