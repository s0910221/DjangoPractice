from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.index, name="index"),
    path('new/', views.new, name="new"),
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('<int:pk>/', views.show, name='show')
]
