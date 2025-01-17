from rest_framework import viewsets

from .models import Book
from .serializers import BookSerializer, BookSerpySerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_serializer_class(self):
        if self.action == "retrieve" or self.action == "list":
            pass
            return BookSerpySerializer

        return self.serializer_class
