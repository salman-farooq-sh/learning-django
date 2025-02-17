from django.urls import path
from rest_framework import renderers
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views4, views5

snippet_list = views5.SnippetViewSet.as_view(
    {
        "get": "list",
        "post": "create",
    }
)
snippet_detail = views5.SnippetViewSet.as_view(
    {
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy",
    }
)
snippet_highlight = views5.SnippetViewSet.as_view(
    {
        "get": "highlight",
    },
    renderer_classes=[renderers.StaticHTMLRenderer],
)
user_list = views5.UserViewSet.as_view(
    {
        "get": "list",
    }
)
user_detail = views5.UserViewSet.as_view(
    {
        "get": "retrieve",
    }
)

urlpatterns = [
    path("", views4.api_root),
    path("snippets/", snippet_list, name="snippet-list"),
    path("snippets/<int:pk>/", snippet_detail, name="snippet-detail"),
    path("snippets/<int:pk>/highlight/", snippet_highlight, name="snippet-highlight"),
    path("users/", user_list, name="user-list"),
    path("users/<int:pk>/", user_detail, name="user-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
