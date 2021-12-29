from django.contrib import admin

# 别忘了导入ArticlerPost
from .models import ArticlePost, ArticleColumn


# 注册ArticlePost到admin中
admin.site.register(ArticlePost)

# 注册动态栏目
admin.site.register(ArticleColumn)