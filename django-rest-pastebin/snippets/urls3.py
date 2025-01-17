from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views3

urlpatterns = [
    path('snippets/', views3.SnippetList.as_view()),
    path('snippets/<int:pk>/', views3.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)