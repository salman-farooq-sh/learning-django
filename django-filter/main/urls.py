from django.urls import path

from .views import BookFilterView, AuthorFilterView

urlpatterns = [
    path('', BookFilterView.as_view(), name='book_filter'),
    path('author_filter/', AuthorFilterView.as_view(), name='author_filter'),
]