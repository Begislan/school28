from django.shortcuts import render, redirect, get_object_or_404
from core.models import BestTcOld
from ..forms import BestTcOldForm

#create
def best_tc_old_create(request):
    if request.method == 'POST':
        form = BestTcOldForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_best_tc_old_list')
    else:
        form = BestTcOldForm()
    return render(request, 'admin/best_tc_old/admin_best_tc_old_create.html', {'form': form})

#list
def best_tc_old_list(request):
    tc = BestTcOld.objects.all()
    return render(request, 'admin/best_tc_old/admin_best_tc_old_list.html', {'tc': tc})

# Update
def best_tc_old_update(request, pk):
    tc = get_object_or_404(BestTcOld, pk=pk)
    if request.method == 'POST':
        form = BestTcOldForm(request.POST, request.FILES, instance=tc)
        if form.is_valid():
            form.save()
            return redirect('admin_best_tc_old_list')
    else:
        form = BestTcOldForm(instance=tc)
    return render(request, 'admin/best_tc_old/admin_best_tc_old_update.html', {'form': form})

# Delete
def best_tc_old_delete(request, pk):
    tc = get_object_or_404(BestTcOld, pk=pk)
    if request.method == 'POST':
        tc.delete()
        return redirect('admin_best_tc_old_list')
    return render(request, 'admin/best_tc_old/admin_best_tc_old_delete.html', {'tc': tc})