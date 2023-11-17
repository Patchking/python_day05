from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.redirect_list, name='redirect-list'),
    path('clientside/', views.get_list, name='get-files-list'),
    path('list/', views.upload_file, name='upload-file'),
    path('list/<str:filename>/', views.get_file, name='get-files-list'),

    # path('/', views.main_page, name='main-page'),
]