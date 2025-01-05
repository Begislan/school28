from django.urls import path
from .views import (admin_core, admin_create_news, admin_detail_news,
                    admin_edit_news, admin_delete_news, admin_teacher,
                    admin_create_teacher, admin_detail_teacher, admin_update_teacher,
                    admin_delete_teacher)


urlpatterns = [
    path('', admin_core, name='admin_core'),
    path('adminCreateNews/', admin_create_news, name='admin_create_news'),
    path('adminDetailNews/<int:id>/', admin_detail_news, name='admin_detail_news'),
    path('editNews/<int:id>/', admin_edit_news, name='admin_edit_news'),
    path('deleteNews/<int:id>/', admin_delete_news, name='admin_delete_news'),

    # teachers
    path('teachers/', admin_teacher, name='admin_teacher'),
    path('teacherCreate/', admin_create_teacher, name='admin_create_teacher'),
    path('teacher/<int:id>/', admin_detail_teacher, name='admin_detail_teacher'),
    path('teacherUpdate/<int:id>/', admin_update_teacher, name='admin_update_teacher'),
    path('teacherDelete/<int:id>/', admin_delete_teacher, name='admin_delete_teacher'),
]