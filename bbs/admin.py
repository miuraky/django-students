from django.contrib import admin

# Register your models here.
from .models import Article # models.pyからArticleクラスをインポート

admin.site.register(Article)    # DjangoAdminにArticleクラスを登録