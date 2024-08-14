from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField

class News(models.Model):
    news_tittle  = models.CharField(max_length=50)
    news_desc = HTMLField()
    news_slug= AutoSlugField(populate_from = 'news_tittle',unique=True,null=True)
    news_image = models.FileField(upload_to="news/",max_length=250,null=True,default=None)