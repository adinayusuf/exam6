from django.urls import path

from webapp.views import index_view, create_view, update_view, delete_view

urlpatterns = [
    path('', index_view, name='index'),
    path('add/', create_view, name='create'),
    path('update/<int:pk>/', update_view, name='update'),
    path('delete/<int:pk>/', delete_view, name='delete')
]
