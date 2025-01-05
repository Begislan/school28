from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from adminka.forms import TeacherForm
from core.models import Teacher


@login_required
@user_passes_test(lambda u: u.is_superuser)
def admin_teacher(request):
    teachers = Teacher.objects.all()
    context = {
        'teachers': teachers,
    }
    return render(request, 'admin/teacher/teacher_core.html', context)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def admin_create_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_teacher')
    else:
        form = TeacherForm()
    return render(request, 'admin/teacher/admin_create_teacher.html', {'form': form})


@login_required
@user_passes_test(lambda u: u.is_superuser)
def admin_detail_teacher(request, id):
    teacher = Teacher.objects.get(id=id)
    context = {
        'teacher': teacher,
    }
    return render(request, 'admin/teacher/admin_detail_teacher.html', context)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def admin_update_teacher(request, id):
    teacher = Teacher.objects.get(id=id)
    if request.method == 'POST':
        form = TeacherForm(request.POST, files=request.FILES, instance=teacher)
        form.is_valid()
        form.save()
        return redirect('admin_detail_teacher', teacher.id)
    else:
        form = TeacherForm(instance=teacher)
    return render(request, 'admin/teacher/admin_update_teacher.html', {'form': form})


@login_required
@user_passes_test(lambda u: u.is_superuser)
def admin_delete_teacher(request, id):
    teacher = Teacher.objects.get(id=id)
    if request.method == 'POST':
        teacher.delete()
        return redirect('admin_teacher')
    return render(request, 'admin/teacher/admin_delete_teacher.html', {'teacher': teacher})
