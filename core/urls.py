from django.urls import path
from core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('teachers/', views.teacher, name='teachers'),
    path('detailNews/<int:pk>', views.detailNews, name='detailNews'),
    path('detailTeacher:<int:pk>', views.detailTeacher, name='detailTeacher'),
    path('bestStudent', views.bestStudents, name='bestStudents'),
    path('bestStudent:<int:pk>', views.detailBestStudents, name='detailBestStudent'),
    path('bestGr', views.bestGr, name='bestGr'),
    path('bestGr:<int:pk>', views.detailBestGr, name='detailBestGr'),
    path('bestTc', views.bestTc, name='bestTc'),
    path('bestTc/<int:pk>', views.detailTc, name='detailTc'),
    path('history/', views.history, name='history'),
]