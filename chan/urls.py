from django.urls import path
from chan import views

urlpatterns = [
    path('',views.chan,name="chan"),
    path('<int:blog_id>/', views.detail, name='chan_detail'),
    path('new/', views.new, name='chan_new'),
    path('create/', views.create, name='chan_create'),
    path('delete/<int:blog_id>',views.delete, name="chan_delete"),
    path('file/<int:blog_id>',views.file,name="chan_file"),
]
