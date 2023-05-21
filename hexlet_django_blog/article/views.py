from django.shortcuts import render
from hexlet_django_blog.article.apps import ArticleConfig
from django.views import View


class IndexView(View):

    app_name = ArticleConfig.name

    def get(self, request, *args, **kwargs):
        return render(request, 'articles/index.html', context={'name': IndexView.app_name})

def index(request):
    app_name = ArticleConfig.name
    return render(request, 'articles/index.html', context={'name': app_name})
