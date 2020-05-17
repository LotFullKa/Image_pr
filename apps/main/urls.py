from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('index/upload_img', views.upload_img, name='upload'),
    path('', views.home, name='home')
]
