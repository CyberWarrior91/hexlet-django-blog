from django.shortcuts import render, redirect
from hexlet_django_blog.article.apps import ArticleConfig
from django.views import View
from django.urls import reverse


class IndexView(View):

    app_name = ArticleConfig.name

    def get(self, request, *args, **kwargs):
        return redirect(reverse('python_article', kwargs={'tags': 'python', 'article_id': 42}))


def article(request, tags: str, article_id: int):
    app_name = ArticleConfig.name
    return render(request, 'articles/index.html', context={'name': app_name, 'tags': tags, 'article_id': article_id})
