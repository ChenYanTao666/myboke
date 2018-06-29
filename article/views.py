from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from datetime import datetime



# Create your views here.
def home(request):
    return HttpResponse('Hello World,yuchen')

def detail(request,my_args):
    list = Article.objects.all()
    if len(list) > int(my_args):
        post = list[int(my_args)]
        str = ("title = %s,category = %s,date_time = %s,content = %s" % (post.title,post.category,post.date_time,post.content))
        return HttpResponse(str)
    else:
        return HttpResponse('没有这个数据哦')
def home(requset):
    post_list = Article.objects.all()
    return render(requset,'home.html',{'post_list':post_list})