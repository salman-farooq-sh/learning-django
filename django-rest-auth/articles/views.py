from rest_framework import generics
from .serializers import ArticleSerializer
from .models import Article


class ArticleListCreateView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
