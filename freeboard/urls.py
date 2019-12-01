from django.urls import path
from freeboard import views

urlpatterns = [
    path('',views.freeboard,name="freeboard"),
    path('<int:blog_id>/', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('delete/<int:blog_id>',views.delete, name="delete"),
    path('file/<int:blog_id>',views.file,name="file"),
]
