from rest_framework import serializers
from django.contrib.auth import get_user_model
from snippets.models import Snippet


class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.IntegerField(source="owner.id", read_only=True)

    class Meta:
        model = Snippet
        fields = ["id", "created", "owner", "title", "code", "linenos", "language", "style"]


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = get_user_model()
        fields = ["id", "username", "snippets"]
