from tabnanny import verbose

from django.db import models
from PIL import Image

class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = "Посты"


class NewsImage(models.Model):
    post = models.ForeignKey(News, related_name='images', on_delete=models.CASCADE)  # Связь с постом
    image = models.ImageField(upload_to='news/', default='default.png')

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
        verbose_name = 'Картина'
        verbose_name_plural = "Каритины"


class Teacher(models.Model):
    name_firstname = models.CharField(max_length=200)
    spec = models.CharField(max_length=120)
    staj = models.CharField(max_length=120)
    img = models.ImageField(upload_to='teacher/', default='default.png')


    def __str__(self):
        return self.name_firstname

    class Meta:
        verbose_name = 'Мугалимдер'
        verbose_name_plural = 'Мугалимдер'


class BestSt(models.Model):
    fio_st = models.CharField(max_length=250, verbose_name='ФИО ученика')
    content_st = models.TextField(verbose_name='Контент необ.', blank=True, null=True)
    klass_st = models.IntegerField(default=1, verbose_name='Класс')
    img_st = models.ImageField(upload_to='best_st/', blank=True, null=True, verbose_name='Фото необ.', default='default.png')

    def __str__(self):
        return self.fio_st

    class Meta:
        verbose_name = 'Мыкты окуучулар'
        verbose_name_plural = 'Мыкты окуучулар'


class BestGr(models.Model):
    fio_gr = models.CharField(max_length=250, verbose_name='ФИО выпускника')
    content_gr = models.TextField(verbose_name='Описние необ.', blank=True, null=True)
    year_gr = models.CharField(max_length=8, verbose_name='Год выпуска')
    img_gr = models.ImageField(upload_to='best_gr/', blank=True, null=True, verbose_name='Фото необ.', default='default.png')

    def __str__(self):
        return self.fio_gr

    class Meta:
        verbose_name = 'Успешные выпускники'
        verbose_name_plural = 'Успешные выпускники'


class BestTcOld(models.Model):
    fio_old_tc = models.CharField(max_length=250, verbose_name='ФИО Пред. оп')
    content_old_tc = models.TextField(verbose_name='Описание необезательно', blank=True, null=True)
    years_old_tc = models.CharField(max_length=20, verbose_name='годами работали')
    srec_old_tc = models.CharField(max_length=20, verbose_name='Специалист')
    img_old_tc = models.ImageField(upload_to='best_teacher_old/', blank=True, null=True, verbose_name='Фото необ.', default='default.png')

    def __str__(self):
        return self.fio_old_tc

    class Meta:
        verbose_name = 'Эмгек синирген мугалимдер'
        verbose_name_plural = 'Эмгек синирен мугалимдер'


class Olimpiada(models.Model):
    title_ol = models.CharField(max_length=250, verbose_name='Заголовка')
    content_ol = models.TextField(verbose_name="Описание необ.", blank=True, null=True)
    img_ol = models.ImageField(upload_to='olimpiada/', blank=True, null=True, verbose_name='фото необ.', default='default.png')

    def __str__(self):
        return self.title_ol

    class Meta:
        verbose_name = 'Олимпиада'
        verbose_name_plural = 'Олимпиада'


class Sport(models.Model):
    title_sp = models.CharField(max_length=255, verbose_name='Заголовка спорт')
    content_sp = models.TextField(verbose_name="Описание необ.", blank=True, null=True)
    img_sp = models.ImageField(upload_to='olimpiada/', blank=True, null=True, verbose_name='фото необ.', default='default.png')

    def __str__(self):
        return self.title_sp

    class Meta:
        verbose_name = 'Спорт'
        verbose_name_plural = 'Спорт'


class EduMatCom(models.Model):
    title_ed = models.CharField(max_length=255, verbose_name="Учебный мет. ком.")
    content_ed = models.TextField(verbose_name='контент необ.', blank=True, null=True)
    img_ed = models.ImageField(upload_to='edumatcom/', verbose_name='фото необ.', blank=True, null=True, default='default.png')

    def __str__(self):
        return self.title_ed
    class Meta:
        verbose_name = 'Уч. мет. ком.'
        verbose_name_plural = 'Уч. мет. ком.'



