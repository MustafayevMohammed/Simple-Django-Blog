from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["id","title","author","created_date"]
    search_fields = ["title"]
    list_filter = ["created_date"]

    class Meta:
        model = models.Article
