from django.db import models

# Create your models here.c
# Create your models here.
class Article(models.Model) :
    title = models.CharField(max_length = 100)  #博客题目
    category = models.CharField(max_length = 50, blank = True)  #博客标签
    date_time = models.DateTimeField(auto_now_add = True)  #博客日期
    content = models.TextField(blank = True, null = True)  #博客文章正文

    #python2使用__unicode__, python3使用__str__
    def __str__(self) :
        return self.title

    class Meta:  #按时间下降排序
        ordering = ['-date_time']



# $ python manage.py makemigrations

# python manage.py migrate #命令行运行该命令   同步数据库

# 出现   表示成功
# Operations to perform:
#   Apply all migrations: auth, sessions, admin, article, contenttypes
# Running migrations:
#   Applying article.0001_initial... OK
#


# shell 操作数据库  增删改查

#
# >>> from article.models import Article
# >>> #create数据库增加操作
# >>> Article.objects.create(title = 'Hello World', category = 'Python', content = 'Let us add a database item')
# <Article: Article object>
# >>> Article.objects.create(title = 'Django Blog Study', category = 'Python', content = 'Django Blog Tutorial')
# <Article: Article object>
#
# >>> #all和get的数据库查看操作
# >>> Article.objects.all()  #查看全部对象, 返回一个列表, 无对象返回空list
# [<Article: Article object>, <Article: Article object>]
# >>> Article.objects.get(id = 1)  #返回符合条件的对象
# <Article: Article object>
#
# >>> #update数据库修改操作
# >>> first = Article.objects.get(id = 1)  #获取id = 1的对象
# >>> first.title
# 'Hello World'
# >>> first.date_time
# datetime.datetime(2014, 12, 26, 13, 56, 48, 727425, tzinfo=<UTC>)
# >>> first.content
# 'Let us add a database item'
# >>> first.category
# 'Python'
# >>> first.content = 'Hello World, How are you'
# >>> first.content  #再次查看是否修改成功, 修改操作就是点语法
# 'Hello World, How are you'
#
# >>> #delete数据库删除操作
# >>> first.delete()
# >>> Article.objects.all()  #此时可以看到只有一个对象了, 另一个对象已经被成功删除
# [<Article: Article object>]
#
# >>>Article.objects.filter(title='Django Blog Study')  # 使用 filter() 按题目过滤
# <QuerySet [<Article: Django Blog Study>]>
#
# >>>Article.objects.filter(title='Django Blog Study', id="1") # 也可以多个条件
# <QuerySet [<Article: Django Blog Study>]>
# #上面是精确匹配 也可以包含性查询
#
# >>>Article.objects.filter(title__contains='Django')
# <QuerySet [<Article: Django Blog Study>]>
#
# #数据排序
# Article.objects.order_by("title")
# Article.objects.order_by("-titile")  # 倒序
#
# #如果需要以多个字段为标准进行排序（第二个字段会在第一个字段的值相同的情况下被使用到），使用多个参数就可以了
# Article.objects.order_by("title", "id")
#
# #连锁查询
# Article.objects.filter(title__contains='Django').order_by("-id")
#
# #限制返回的数据数量
# Article.objects.filter(title__contains='Django')[0]
# Article.objects.filter(title__contains='Django')[0:3]  #可以进行类似于列表的操作


