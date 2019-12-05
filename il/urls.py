from django.urls import path
from il import views

urlpatterns = [
    path('',views.il,name="il"),
    path('<int:blog_id>/', views.detail, name='il_detail'),
    path('new/', views.new, name='il_new'),
    path('create/', views.create, name='il_create'),
    path('delete/<int:blog_id>',views.delete, name="il_delete"),
    path('file/<int:blog_id>',views.file,name="il_file"),
]
