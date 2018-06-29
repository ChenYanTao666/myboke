from django.contrib import admin
from article.models import Article
# Register your models here.
#注册才能在管理也查看修改
admin.site.register(Article)