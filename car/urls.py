from django.urls import path

from .views import create, delete, detail, home, search, update

urlpatterns = [
    path('', home, name='home'),
    path('detail/<int:pk>/', detail, name='detail'),
    path('create/', create, name='create'),
    path('update/<int:pk>/', update, name='update'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('search/', search, name='search'),
]