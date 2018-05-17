from django.conf.urls import url
from . import views
from django.urls import include, path

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<pk>/', views.post_detail, name='post_detail'),
]
