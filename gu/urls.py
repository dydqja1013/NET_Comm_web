from django.urls import path
from gu import views

urlpatterns = [
    path('',views.gu,name="gu"),
    path('<int:blog_id>/', views.detail, name='gu_detail'),
    path('new/', views.new, name='gu_new'),
    path('create/', views.create, name='gu_create'),
    path('delete/<int:blog_id>',views.delete, name="gu_delete"),
    path('file/<int:blog_id>',views.file,name="gu_file"),
]
