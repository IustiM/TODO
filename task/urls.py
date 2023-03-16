from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('update-list/<str:pk>/', views.update_list, name='update-list'),
    path('confirm/<str:pk>/', views.delTask, name='confirm'),
]
