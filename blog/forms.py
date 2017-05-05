from django import forms
from .models import Article, BlogComment


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        exclude = ('author', 'timestamp', 'publish')


class CommentForm(forms.ModelForm):

    content = forms.CharField(widget=forms.Textarea(attrs={'class': "form-control", 'rows': "3"}))

    class Meta:
        model = BlogComment
        fields = ('content',)
        exclude = ('author', 'comment_on', 'timestamp')
