from django.shortcuts import render, redirect
from core.models import News, NewsImage
from django.core.paginator import Paginator
from django.db.models import Q
from ..forms import NewsForm, NewsImageFormSet, NewsImageForm
from datetime import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test


# Create your views here.
@login_required
@user_passes_test(lambda u: u.is_superuser)
def admin_core(request):
    all_data = News.objects.all().order_by('-id')
    return render(request, 'admin/news/admin_core.html', {
        'all_data': all_data
    })


@login_required
@user_passes_test(lambda u: u.is_superuser)
def admin_create_news(request):
    current_time = datetime.now()  # Текущая дата и время

    if request.method == 'POST':
        form = NewsForm(request.POST)
        formset = NewsImageFormSet(request.POST, request.FILES, queryset=NewsImage.objects.none())

        if form.is_valid() and formset.is_valid():
            post = form.save()  # Сохраняем объект Post

            # Сохраняем каждое изображение, связанное с постом
            for form in formset.cleaned_data:
                if form:
                    image = form['image']
                    NewsImage.objects.create(post=post, image=image)
            return redirect('admin_core')  # Перенаправляем на страницу успешного выполнения
    else:
        form = NewsForm()
        formset = NewsImageFormSet(queryset=NewsImage.objects.none())

    context = {
        'form': form,
        'formset': formset,
        'current_time': current_time,
    }

    return render(request, 'admin/news/admin_create_news.html', context)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def admin_detail_news(request, id):
    post = News.objects.prefetch_related('images').get(id=id)
    context = {
        'post': post,
    }
    return render(request, 'admin/news/admin_detail_news.html', context)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def admin_edit_news(request, id):
    post = get_object_or_404(News, id=id)  # Получаем существующий пост
    current_time = datetime.now()  # Текущая дата и время

    if request.method == 'POST':
        form = NewsForm(request.POST, instance=post)  # Передаем существующий объект post в форму

        if form.is_valid():
            form.save()  # Сохраняем только текстовые данные поста
            return redirect('admin_detail_news', id=post.id)  # Перенаправляем на детальную страницу поста
        else:
            print(f"Form errors: {form.errors}")
    else:
        form = NewsForm(instance=post)  # Загружаем существующие данные поста

    context = {
        'form': form,
        'post': post,
        'current_time': current_time,  # Передаем текущую дату и время, если нужно для шаблона
    }

    return render(request, 'admin/news/admin_edit_news.html', context)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def admin_delete_news(request, id):
    post = get_object_or_404(News, id=id)  # Получаем пост по ID
    if request.method == 'POST':  # Если запрос POST, удаляем пост
        post.delete()
        return redirect('admin_core')  # После удаления перенаправляем на список всех постов

    context = {
        'post': post,  # Передаем пост в шаблон для подтверждения удаления
    }
    return render(request, 'admin/news/admin_delete_news.html', context)
