import serpy
import zoneinfo
from django.conf import settings
from rest_framework.settings import api_settings


class IntField(serpy.IntField):
    def to_value(self, value):
        if value is not None:
            return super().to_value(value)


class StrField(serpy.StrField):
    def to_value(self, value):
        if value is not None:
            return super().to_value(value)


class BoolField(serpy.BoolField):
    def to_value(self, value):
        if value is not None:
            return super().to_value(value)


class DateTimeField(serpy.Field):
    def to_value(self, datetime):
        if datetime is not None:
            if settings.USE_TZ and True:
                datetime = datetime.astimezone(zoneinfo.ZoneInfo(settings.TIME_ZONE))

            return datetime.strftime(api_settings.DATETIME_FORMAT)


class ForeignKeyRelatedField(serpy.Field):
    def to_value(self, value):
        if value is not None:
            return value.pk


class ManyRelatedField(serpy.Field):
    def to_value(self, value):
        if value is not None:
            return list(value.all().values_list("pk", flat=True))


class ManyStringRelatedField(serpy.Field):
    def to_value(self, value):
        if value is not None:
            return [str(bc) for bc in value.all()]


class FileField(serpy.Field):
    def to_value(self, value):
        if value is not None:
            return value.url


ImageField = FileField
DecimalField = StrField
JSONField = serpy.Field


class ContextSerializer(serpy.Serializer):
    def __init__(self, *args, **kwargs):
        super(ContextSerializer, self).__init__(*args, **kwargs)
        if "context" in kwargs:
            self.context = kwargs["context"]
