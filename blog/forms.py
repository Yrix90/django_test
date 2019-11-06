from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    """Класс для определения модели формы для сайта"""

    class Meta:
        model = Post
        fields = ('title', 'text',)