from django.urls import path
from jun import views

urlpatterns = [
    path('',views.jun,name="jun"),
    path('<int:blog_id>/', views.detail, name='jun_detail'),
    path('new/', views.new, name='jun_new'),
    path('create/', views.create, name='jun_create'),
    path('delete/<int:blog_id>',views.delete, name="jun_delete"),
    path('file/<int:blog_id>',views.file,name="jun_file"),
]
