from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('authors/', views.authors, name='authors'),
    path('authors/<int:author_id>', views.author, name='author'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('books/<int:pk>', views.BookDetailView.as_view(), name='book'),
    path('search/', views.search, name='search'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('i18n/', include('django.conf.urls.i18n')),
    path('user_books/', views.UserBookListView.as_view(), name='user_books'),
    path('user_books/<int:pk>', views.UserBookDetailView.as_view(), name='user_book'),
    path('user_books/new', views.UserBookCreateView.as_view(), name='user_book_new'),
    path('user_books/<int:pk>/update', views.UserBookUpdateView.as_view(), name='user_book_update'),
    path('user_books/<int:pk>/delete', views.UserBookDeleteView.as_view(), name='user_book_delete'),
]