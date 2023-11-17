from django.urls import path
from . import views

urlpatterns = [
    path('push/', views.upload_file, name='upload-file'),
    path('list/', views.get_list, name='files-list'),
]