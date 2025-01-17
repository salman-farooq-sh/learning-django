from rest_framework import serializers
import serpy

from . import serpy_fields
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    foo = serializers.JSONField(source="foo_dict")

    class Meta:
        model = Book
        fields = '__all__'
        # fields = [
        #     "id",
        #     "title",
        #     "publication_date",
        #     "author",
        #     "categories",
        #     "price",
        #     "foo",
        # ]


class BookSerpySerializer(serpy.Serializer):
    id = serpy.IntField()
    title = serpy_fields.StrField()
    publication_date = serpy_fields.DateTimeField()
    author = serpy_fields.ForeignKeyRelatedField()
    # categories = serpy_fields.ManyToManyField()
    categories = serpy_fields.ManyStringRelatedField()
    price = serpy_fields.StrField()
    foo = serpy.Field(attr="foo_dict")

    def to_value(self, instance):
        data = super().to_value(instance)
        return data
