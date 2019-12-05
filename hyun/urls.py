from django.urls import path
from hyun import views

urlpatterns = [
    path('',views.hyun,name="hyun"),
    path('<int:blog_id>/', views.detail, name='hyun_detail'),
    path('new/', views.new, name='hyun_new'),
    path('create/', views.create, name='hyun_create'),
    path('delete/<int:blog_id>',views.delete, name="hyun_delete"),
    path('file/<int:blog_id>',views.file,name="hyun_file"),
]
