from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    """Класс для определения модели формы для сайта"""

    class Meta:
        model = Post
        fields = ('title', 'text',)


class CommentForm(forms.ModelForm):
    """Класс формы для коментариев"""

    class Meta:
        model = Comment
        fields = ('author', 'text',)


class CommentInput(forms.ModelForm):
    """Класс для ввода комментариев под постом"""

    class Meta:
        model = Comment
        fields = ('text',)
        label = {'text': 'Введите Ваш комментарий'}
