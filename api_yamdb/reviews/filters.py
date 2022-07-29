import django_filters

from .models import Title


class TitleFilter(django_filters.FilterSet):
    """Класс фильтра для тайтлов."""
    genre = django_filters.CharFilter(field_name='genre', lookup_expr='slug')
    category = django_filters.CharFilter(
        field_name='category',
        lookup_expr='slug'
    )
    year = django_filters.NumberFilter(field_name='year')
    name = django_filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Title
        fields = ('genre', 'category', 'year', 'name',)
