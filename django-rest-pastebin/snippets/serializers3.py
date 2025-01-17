from rest_framework import serializers
from django.contrib.auth import get_user_model
from snippets.models import Snippet


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    # owner = serializers.CharField(source="owner.username", read_only=True)
    owner = serializers.HyperlinkedRelatedField(view_name="user-detail", read_only=True)
    highlight = serializers.HyperlinkedIdentityField(view_name="snippet-highlight", format="html")

    class Meta:
        model = Snippet
        fields = [
            "url",
            "id",
            "highlight",
            "created",
            "owner",
            "title",
            "code",
            "linenos",
            "language",
            "style",
        ]


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name="snippet-detail", read_only=True)

    class Meta:
        model = get_user_model()
        fields = ["url", "id", "username", "snippets"]
