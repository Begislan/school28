from django.shortcuts import render, redirect
from database.models import News
from .forms import NewsCreateForm

# Create your views here.
def admin_core(request):
    all_data = News.objects.all()
    return render(request, 'admin/admin_core.html', {
        'all_data': all_data
    })

def admin_create_news(request):
    
    if request.method == "POST":
        form = NewsCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_core')
    else:
        form = NewsCreateForm
    return render(request, 'admin/admin_create_news.html', {'form':form})
        

def admin_detail_news(request, id):
    data = News.objects.get(id=id)
    context = {
        "data": data
    }
    return render(request, 'admin/admin_detail_news.html', context)
