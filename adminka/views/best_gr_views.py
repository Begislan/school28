from django.shortcuts import render, redirect, get_object_or_404

from core.models import BestGr
from ..forms import BestGrForm


# Create
def best_gr_create(request):
    if request.method == 'POST':
        form = BestGrForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_best_gr_list')
    else:
        form = BestGrForm()
    return render(request, 'admin/best_gr/admin_best_gr_form.html', {'form': form})

# Read (List)
def best_gr_list(request):
    gradients = BestGr.objects.all()
    return render(request, 'admin/best_gr/admin_best_gr.html', {'gradients': gradients})

# Update
def best_gr_update(request, pk):
    gradient = get_object_or_404(BestGr, pk=pk)
    if request.method == 'POST':
        form = BestGrForm(request.POST, request.FILES, instance=gradient)
        if form.is_valid():
            form.save()
            return redirect('admin_best_gr_list')
    else:
        form = BestGrForm(instance=gradient)
    return render(request, 'admin/best_gr/admin_best_gr_update.html', {'form': form})

# Delete
def best_gr_delete(request, pk):
    gradient = get_object_or_404(BestGr, pk=pk)
    if request.method == 'POST':
        gradient.delete()
        return redirect('admin_best_gr_list')
    return render(request, 'admin/best_gr/admin_best_gr_delete.html', {'gradient': gradient})