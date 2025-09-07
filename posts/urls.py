from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_create, name='post_create'),
    path('post/<int:pk>/edit/', views.post_update,name='post_update'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('aloqa/', views.aloqa, name='aloqa'),
    path('about/', views.about, name='about_us'),
  ]


#karta_num = 98 60 35 01 46 71 49 50