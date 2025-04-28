from django_filters.rest_framework import CharFilter, FilterSet

from titles.models import Title


class TitleFilter(FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    category = CharFilter(field_name='category__slug')
    genre = CharFilter(field_name='genre__slug')

    class Meta:
        model = Title
        fields = ('name', 'category', 'genre', 'year',)
