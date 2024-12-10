from django.http import HttpResponse

from django.shortcuts import render
from .models import News
# Create your views here.


def index(request):
    data = News.objects.all()
    context = {
        'data': data
    }
    return render(request, 'index.html', context)