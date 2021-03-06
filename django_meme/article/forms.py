# 引入表单类
from django import forms
# 引入动态模型
from .models import ArticlePost


# 写动态的表单类
class ArticlePostForm(forms.ModelForm):
    class Meta:
        # 指明数据模型来源
        model = ArticlePost
        # 定义表单包含的字段
        fields = ('title', 'body', 'tags', 'avatar')