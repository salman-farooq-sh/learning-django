from rest_framework import permissions
from rest_framework import viewsets, renderers
from rest_framework.decorators import action
from rest_framework.response import Response

from django.contrib.auth import get_user_model

from snippets.models import Snippet
from snippets.permissions import IsOwnerOrReadOnly
from snippets.serializers3 import SnippetSerializer, UserSerializer


class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    @action(
        detail=True,
        renderer_classes=[renderers.StaticHTMLRenderer],
    )
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
