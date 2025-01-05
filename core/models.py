from django.db import models
from PIL import Image

class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created_at']
        verbose_name = 'Пост'
        verbose_name_plural = "Посты"


class NewsImage(models.Model):
    post = models.ForeignKey(News, related_name='images', on_delete=models.CASCADE)  # Связь с постом
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f'Image for {self.post.title}'

    def save(self, *args, **kwargs):
        super(NewsImage, self).save(*args, **kwargs)
        img = Image.open(self.image.path)  # Уменьшаем размер изображения для экономии памяти
        img = img.convert("RGB")
        output_size = (800, 800)
        img.thumbnail(output_size, Image.LANCZOS)
        img.save(self.image.path, quality=85, optimize=True)

    class Meta:
        ordering = ['post']
        verbose_name = 'Картина'
        verbose_name_plural = "Каритины"


class Teacher(models.Model):
    name_firstname = models.CharField(max_length=200)
    spec = models.CharField(max_length=120)
    staj = models.CharField(max_length=120)
    img = models.ImageField(upload_to='teacher/')


    def __str__(self):
        return self.name_firstname

    class Meta:
        verbose_name = 'Мугалимдер'
        verbose_name_plural = 'Мугалимдер'