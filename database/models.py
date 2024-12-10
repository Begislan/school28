from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=250, verbose_name='Заголовка')

    content = models.TextField(verbose_name='Контент')
    content_full = models.TextField(verbose_name='полный контент')
    data_create = models.DateField(auto_now=True, verbose_name='Дата создание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Новости'
        verbose_name_plural='Новости'