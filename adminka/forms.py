from django import forms
from core.models import News, NewsImage, Teacher
from django.forms import modelformset_factory

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'created_at']  # Поля для поста

class NewsImageForm(forms.ModelForm):
    class Meta:
        model = NewsImage
        fields = ['image']  # Поле для загрузки изображения


NewsImageFormSet = modelformset_factory(NewsImage, form=NewsImageForm, extra=10)  # Можно загрузить до 10 изображений


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'