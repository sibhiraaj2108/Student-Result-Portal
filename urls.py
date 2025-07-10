from django.contrib import admin
from django.urls import path
from results import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.result_list, name='result_list'),
    path('add/', views.result_create, name='result_add'),
    path('edit/<int:pk>/', views.result_update, name='result_edit'),
    path('delete/<int:pk>/', views.result_delete, name='result_delete'),
]