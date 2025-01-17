from django.urls import path
from .views import ArticleListCreateView

urlpatterns = [
    path("", ArticleListCreateView.as_view()),
]
