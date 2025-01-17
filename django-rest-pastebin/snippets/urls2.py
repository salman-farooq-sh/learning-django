from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views2

urlpatterns = [
    path('snippets/', views2.SnippetList.as_view()),
    path('snippets/<int:pk>/', views2.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)