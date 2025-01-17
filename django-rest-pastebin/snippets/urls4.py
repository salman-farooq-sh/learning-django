from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views4

urlpatterns = [
    path("", views4.api_root),
    path("snippets/", views4.SnippetList.as_view(), name="snippet-list"),
    path("snippets/<int:pk>/", views4.SnippetDetail.as_view(), name="snippet-detail"),
    path("snippets/<int:pk>/highlight/", views4.SnippetHighlight.as_view(), name="snippet-highlight"),
    path("users/", views4.UserList.as_view(), name="user-list"),
    path("users/<int:pk>/", views4.UserDetail.as_view(), name="user-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
