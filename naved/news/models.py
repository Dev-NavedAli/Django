from django.db import models
from tinymce.models import HTMLField

class News(models.Model):
    news_tittle  = models.CharField(max_length=50)
    news_desc = HTMLField()
# Create your models here.
