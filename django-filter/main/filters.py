import django_filters
from django import forms
from .models import Book, Genre, Author


class BookFilter(django_filters.FilterSet):
    class Meta:
        model = Book
        fields = {
            'price': ['gte', 'lte'],
            'publication_date': ['year__exact', 'year__gte', 'year__lte'],
            'title': ['icontains'],
            'isbn': ['exact'],
            'summary': ['icontains'],
            'author__name': ['icontains'],
        }

    genres = django_filters.ModelMultipleChoiceFilter(
        queryset=Genre.objects.all(),
        method='filter_genres',
        widget=forms.CheckboxSelectMultiple,
    )

    def filter_genres(self, queryset, name, values):
        if not values:
            return queryset

        querysets = []
        for value in values:
            q = queryset.filter(**{name: value})
            if q.count() == 0:
                return q
            querysets.append(q)

        return querysets[0].intersection(*querysets[1:])
