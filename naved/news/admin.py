from django.contrib import admin
from news.models import News

class NewsAdmin(admin.ModelAdmin):
    list_display = ('news_tittle','news_desc')

admin.site.register(News,NewsAdmin)
# Register your models here.
