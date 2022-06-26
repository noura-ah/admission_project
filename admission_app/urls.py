from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('dashboard',views.dashboard),
    path('logout',views.logout),
    path('admin',views.admin),
    path('add_course',views.add_course)

]