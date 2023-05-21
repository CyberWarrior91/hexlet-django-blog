from django.shortcuts import render
from hexlet_django_blog.article.apps import ArticleConfig


def index(request):
    app_name = ArticleConfig.name
    return render(request, 'articles/index.html', context={'name': app_name})
