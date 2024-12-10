from django import forms
from database.models import News

class NewsCreateForm(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'