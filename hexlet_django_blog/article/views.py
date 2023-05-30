from django.shortcuts import render, get_object_or_404, redirect
from hexlet_django_blog.article.apps import ArticleConfig
from django.views import View
from django.urls import reverse
from hexlet_django_blog.article.models import Article
from .forms import CommentArticleForm, ArticleForm
from django.http import HttpResponseRedirect
from django.contrib.messages import get_messages
from django.contrib import messages


class IndexView(View):

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, 'articles/index.html', context={
            'articles': articles,
        })

class ArticleView(View):

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(request, 'articles/show.html', context={
            'article': article,
        })

class CommentArticleView(View):

    def get(self, request, *args, **kwargs):
        form = CommentArticleForm() # Создаем экземпляр нашей формы
        return render(request, 'articles/comment.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = CommentArticleForm(request.POST) # Получаем данные формы из запроса
        if form.is_valid(): # Проверяем данные формы на корректность
            comment = Comment(
                name = form.cleaned_data['content'], # Получаем очищенные данные из поля content
                        # Заполняем оставшиеся поля
                )
            comment.save()

class ArticleFormCreateView(View):

    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        messages = get_messages(request)
        return render(request, 'articles/create.html', {'form': form, 'messages': messages})

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid(): # Если данные корректные, то сохраняем данные формы
            form.save()
            messages.success(request, 'The article has been created successfully')
            return redirect(reverse('articles')) # Редирект на указанный маршрут
        # Если данные некорректные, то возвращаем человека обратно на страницу с заполненной формой
        messages.add_message(request, messages.ERROR, 'The data is incorrect')
        return render(request, 'articles/create.html', {'form': form})

class ArticleFormEditView(View):

    def get(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(instance=article)
        messages = get_messages(request)
        return render(request, 'articles/update.html', context={
            'form': form, 'article_id':article_id, 'messages': messages,})

    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, 'The article has been updated successfully')
            return redirect('articles')
        messages.add_message(request, messages.ERROR, 'The data is incorrect')
        return render(request, 'articles/update.html', {'form': form, 'article_id':article_id})

class ArticleFormDestroyView(View):

    def post(self, request, *args, **kwargs):
        article_id = int(kwargs.get('id'))
        article = Article.objects.get(id=article_id)
        if article:
            article.delete()
            messages.success(request, 'The article has been deleted successfully')
        return redirect('articles')
