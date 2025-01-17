from rest_framework import permissions, viewsets

from .models import Post
from .permissions import IsAuthorOrReadOnly, IsLoggedInUserTheAuthor
from .serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsLoggedInUserTheAuthor,
        IsAuthorOrReadOnly,
    )
    queryset = Post.objects.all()
    serializer_class = PostSerializer
