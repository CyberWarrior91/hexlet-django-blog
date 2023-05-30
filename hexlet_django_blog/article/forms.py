from django import forms
from django.forms import ModelForm # Импортируем формы Django
from .models import Article

class CommentArticleForm(forms.Form):
    content = forms.CharField(label='Комментарий', widget=forms.Textarea)

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'body']
