from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('addbook/', views.AddBooks.as_view(), name='addbook_url'),
    path('addauthor/', views.AddAuthor.as_view(), name='author_url'),
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('author/', views.Authors.as_view(), name='author'),
    path('search/', views.search, name='search'), 
    path('<int:pk>/', views.BookDetail.as_view(), name='book_detail'),
]