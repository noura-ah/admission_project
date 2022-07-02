from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('home',views.home),
    path('logout',views.logout),
    path('admin',views.admin),
    path('add_course',views.add_course),
    path('edit_state/<int:id>/<str:state>',views.edit_state),
    path('apply_course/<int:id>',views.apply_course),
    path('student_profile/<int:id>',views.show_student),
    path('delete_course/<int:id>',views.delete_course),
    path('edit_course/<int:id>',views.edit_course),
    path('edit_profile',views.edit_profile),
    path('add_message',views.add_message),
    path('show_message',views.show_message),
    path('read_message/<int:id>',views.read_message),
    path('admin/<int:id>',views.show_students_course)

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
