from django.urls import path
from .views import (admin_core, admin_create_news, admin_detail_news,
                    admin_edit_news, admin_delete_news,

                    admin_teacher, admin_create_teacher, admin_detail_teacher,
                    admin_update_teacher, admin_delete_teacher,

                    best_st_create, best_st_list, best_st_update, best_st_delete,

                    best_gr_list, best_gr_create, best_gr_update,best_gr_delete,

                    best_tc_old_create, best_tc_old_list, best_tc_old_update, best_tc_old_delete
                    )


urlpatterns = [
    path('', admin_core, name='admin_core'),
    path('CreateNews/', admin_create_news, name='admin_create_news'),
    path('DetailNews/<int:id>/', admin_detail_news, name='admin_detail_news'),
    path('EditNews/<int:id>/', admin_edit_news, name='admin_edit_news'),
    path('DeleteNews/<int:id>/', admin_delete_news, name='admin_delete_news'),

    # teachers
    path('Teachers/', admin_teacher, name='admin_teacher'),
    path('TeacherCreate/', admin_create_teacher, name='admin_create_teacher'),
    path('Teacher/<int:id>/', admin_detail_teacher, name='admin_detail_teacher'),
    path('TeacherUpdate/<int:id>/', admin_update_teacher, name='admin_update_teacher'),
    path('TeacherDelete/<int:id>/', admin_delete_teacher, name='admin_delete_teacher'),

    # best_st
    path('St', best_st_list, name='admin_best_st_list'),
    path('StCreate/', best_st_create, name='admin_best_st_create'),
    path('St<int:pk>/update/', best_st_update, name='admin_best_st_update'),
    path('St<int:pk>/delete/', best_st_delete, name='admin_best_st_delete'),

    #best_gr
    path('Gr', best_gr_list, name='admin_best_gr_list'),
    path('GrCreate/', best_gr_create, name='admin_best_gr_create'),
    path('GrUpdate/<int:pk>/', best_gr_update, name='admin_best_gr_update'),
    path('GrDelete/<int:pk>/', best_gr_delete, name='admin_best_gr_delete'),

    #best_tc_old
    path('Tc', best_tc_old_list, name='admin_best_tc_old_list'),
    path('TcCreate/', best_tc_old_create, name='admin_best_tc_old_create'),
    path('TcUpdate/<int:pk>/', best_tc_old_update, name='admin_best_tc_old_update'),
    path('TcDelete/<int:pk>', best_tc_old_delete, name='admin_best_tc_old_delete'),

]