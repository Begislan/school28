from django.shortcuts import render
from .models import (News, Teacher, BestSt, BestGr, BestTcOld)
from django.shortcuts import render, get_object_or_404


# Core
def home(request):
    # News
    latest_news = News.objects.prefetch_related('images').order_by('-created_at')  # [:3]

    # Готовим посты с первыми изображениями
    posts_with_images = []
    for post in latest_news:
        first_image = post.images.first()  # Получаем первое связанное изображение
        posts_with_images.append({
            'post': post,
            'image': first_image.image.url if first_image else None
        })

    # Teachers
    teachers = Teacher.objects.all()[:4]

    # Best students
    students = BestSt.objects.all()[:4]

    # best gr
    gr = BestGr.objects.all()[:4]

    # best tc old
    old = BestTcOld.objects.all()[:4]

    context = {
        'posts_with_images': posts_with_images,
        'teachers': teachers,
        'students': students,
        'gr': gr,
        'old': old,
    }
    return render(request, 'core/index.html', context)


# About
def teacher(request):
    teacher = Teacher.objects.all()

    context = {
        'teacher': teacher,
    }

    return render(request, 'core/about/teacher.html', context)


def detailNews(request, pk):
    post = News.objects.get(pk=pk)
    images = post.images.all()
    return render(request, 'core/detail/detailNews.html', {'post': post, 'images': images})


def detailTeacher(request, pk):
    teacher = Teacher.objects.get(pk=pk)
    context = {
        'teacher': teacher,
    }
    return render(request, 'core/detail/detailTeachers.html', context)


def bestStudents(request):
    students = BestSt.objects.all()
    return render(request, 'core/about/bestStudents.html', {'students': students})


def detailBestStudents(request, pk):
    student = BestSt.objects.get(pk=pk)
    return render(request, 'core/detail/detailBestStudents.html', {'student': student})


def bestGr(request):
    gr = BestGr.objects.all()
    return render(request, 'core/about/bestGr.html', {'gr': gr})


def detailBestGr(request, pk):
    gr = BestGr.objects.get(pk=pk)
    return render(request, 'core/detail/detailGr.html', {'gr': gr})


def bestTc(request):
    tc = BestTcOld.objects.all()
    return render(request, 'core/about/bestTs.html', {'tc': tc})


def detailTc(request, pk):
    tc = BestTcOld.objects.get(pk=pk)
    context = {
        'tc': tc,
    }
    return render(request, 'core/detail/detailTcOld.html', context)

def history(request):
    return render(request, 'core/about/history.html')
