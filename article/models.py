from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Article(models.Model):
    author = models.ForeignKey("auth.user",on_delete=CASCADE,verbose_name="Yazici:")
    title = models.CharField(max_length=30,verbose_name="Basliq:")
    content = models.TextField(verbose_name="Mezmun:")
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Yazilma Tarixi:")

    def __str__(self):
        return self.title