from django.shortcuts import render, redirect, get_object_or_404
from core.models import BestSt
from ..forms import BestStForm

# Create
def best_st_create(request):
    if request.method == 'POST':
        form = BestStForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_best_st_list')
    else:
        form = BestStForm()
    return render(request, 'admin/best_st/admin_best_st_form.html', {'form': form})

# Read (List)
def best_st_list(request):
    students = BestSt.objects.all()
    return render(request, 'admin/best_st/admin_best_st.html', {'students': students})

# Update
def best_st_update(request, pk):
    student = get_object_or_404(BestSt, pk=pk)
    if request.method == 'POST':
        form = BestStForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('admin_best_st_list')
    else:
        form = BestStForm(instance=student)
    return render(request, 'admin/best_st/admin_best_st_update.html', {'form': form})

# Delete
def best_st_delete(request, pk):
    student = get_object_or_404(BestSt, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('admin_best_st_list')
    return render(request, 'admin/best_st/admin_best_st_delete.html', {'student': student})
