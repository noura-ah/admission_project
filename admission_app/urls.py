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
    path('add_course',views.add_course),
    path('edit_state/<int:id>/<str:state>',views.edit_state),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)