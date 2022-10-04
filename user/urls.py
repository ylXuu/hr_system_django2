from django.urls import path,include
from . import views
from django.conf.urls import url

urlpatterns = [
    path('',views.login,name='login'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('worker_index/',views.worker_index,name='worker_index'),
    path('worker_attend/',views.worker_attend,name='worker_attend'),
    path('am_in/',views.am_in,name='am_in'),
    path('am_off/',views.am_off,name='am_off'),
    path('pm_in/',views.pm_in,name='pm_in'),
    path('pm_off/',views.pm_off,name='pm_off'),
    path('worker_all_train/',views.worker_all_train,name='worker_all_train'),
    url(r'^sign_up/(\d+)/$',views.sign_up,name='sign_up'),
    path('worker_train/',views.worker_train,name='worker_train'),
    path('worker_salary_award/',views.worker_salary_award,name='worker_salary_award'),
    path('worker_performance_plan/',views.worker_performance_plan,name='worker_performance_plan'),
    path('worker_performance/',views.worker_performance,name='worker_performance'),
    path('worker_account_safe/',views.worker_account_safe,name='worker_account_safe'),
    path('worker_modify_password/',views.worker_modify_password,name='worker_modify_password'),


    path('admin_login/',views.admin_login,name='admin_login'),
    path('admin_index/',views.admin_index,name='admin_index'),
    path('admin_create_attend/',views.admin_create_attend,name='admin_create_attend'),#已创建-失效按钮
    path('create_table/',views.create_table,name='create_table'),
    path('admin_today_attend/',views.admin_today_attend,name='admin_today_attend'),
    path('admin_history_attend/',views.admin_history_attend,name='admin_history_attend'),
    url(r'^admin_view_history/(\w+)/$',views.admin_view_history,name='admin_view_history'),
    url(r'^admin_delete_history/(\w+)/$',views.admin_delete_history,name='admin_delete_history'),
    path('admin_train/',views.admin_train,name='admin_train'),
    url(r'^admin_view_train_worker/(\d+)/$',views.admin_view_train_worker,name='admin_view_train_worker'),
    url(r'^delete_train_worker/(\d+)&(\d+)/$',views.delete_train_worker,name='delete_train_worker'),
    path('admin_create_train/',views.admin_create_train,name='admin_create_train'),
    path('admin_worker_in/',views.admin_worker_in,name='admin_worker_in'),
    path('admin_add_worker/',views.admin_add_worker,name='admin_add_worker'),
    url(r'^admin_edit_worker/(\d+)/$',views.admin_edit_worker,name='admin_edit_worker'),
    url(r'^admin_initial_password/(\d+)/$',views.admin_initial_password,name='admin_initial_password'),
    path('admin_do_edit/',views.admin_do_edit,name='admin_do_edit'),
    url(r'^admin_quit_worker/(\d+)/$',views.admin_quit_worker,name='admin_quit_worker'),
    path('admin_do_quit/',views.admin_do_quit,name='admin_do_quit'),
    path('admin_worker_out/',views.admin_worker_out,name='admin_worker_out'),
    path('search_by_id/',views.search_by_id,name='search_by_id'),
    path('search_by_name/',views.search_by_name,name='search_by_name'),
    path('search_by_department/',views.search_by_department,name='search_by_department'),
    path('search_by_id_out/',views.search_by_id_out,name='search_by_id_out'),
    path('search_by_name_out/',views.search_by_name_out,name='search_by_name_out'),
    path('search_by_department_out/',views.search_by_department_out,name='search_by_department_out'),
    path('admin_recruit/',views.admin_recruit,name='admin_recruit'),
    path('admin_salary/',views.admin_salary,name='admin_salary'),
    url(r'^admin_modify_salary/(\d+)&(\d+)/$',views.admin_modify_salary,name='admin_modify_salary'),
    path('admin_do_modify/',views.admin_do_modify,name='admin_do_modify'),
    path('admin_award/',views.admin_award,name='admin_award'),
    path('admin_add_award/',views.admin_add_award,name='admin_add_award'),
    path('admin_do_add/',views.admin_do_add,name='admin_do_add'),
    path('admin_performance/',views.admin_performance,name='admin_performance'),
    path('admin_assessment/',views.admin_assessment,name='admin_assessment'),
    #path('admin_account_safe/'),

]