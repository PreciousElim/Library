from django.urls import path
from .views import BookView, BookDetailView



urlpatterns = [
    path('book/', BookView.as_view(), name = 'book-list'),
    path('book/<int:pk>/', BookDetailView.as_view(), name = 'book-details')
]