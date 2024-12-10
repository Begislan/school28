from django.urls import path
from .views import admin_core, admin_create_news, admin_detail_news


urlpatterns = [
    path('', admin_core, name='admin_core'),
    path('adminCreateNews/', admin_create_news, name='admin_create_news'),
    path('adminDetailNews/<int:id>', admin_detail_news, name='admin_detail_news')
]