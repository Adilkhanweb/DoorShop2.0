from django_filters.widgets import *

from shop.models import *
import django_filters

# class CharFilterInFilter(django_filters.BaseInFilter, django_filters.CharFilter):
#     pass


CHOICES = (
    ('descending', 'От Я до А'),
    ('price_low_to_high', 'Цена по возростанию'),
    ('price_high_to_low', 'Цена по убыванию'),
)

COLORS = Variants.objects.all().values_list('color__name', 'color__name').distinct()
TYPES = DoorType.objects.all().values_list('type', 'type')


class VariantsFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains', label="Название двери:",
                                      widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Прим...'}))
    ordering = django_filters.ChoiceFilter(label="Порядок", choices=CHOICES,
                                           method='filter_by_order', null_value='ascending',
                                           empty_label="От А до Я",
                                           widget=forms.Select(attrs={'class': 'form-control'}))
    min_price = django_filters.NumberFilter(field_name='sale_price', lookup_expr='gte', label='Мин. цена',
                                            widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'number',
                                                                          'placeholder': int(
                                                                              Variants.objects.all().order_by(
                                                                                  'sale_price').first().sale_price)}))
    max_price = django_filters.NumberFilter(field_name='sale_price', lookup_expr='lte', label='Макс. цена',
                                            widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'number',
                                                                          'placeholder': int(
                                                                              Variants.objects.all().order_by(
                                                                                  '-sale_price').first().sale_price)}))
    color = django_filters.ChoiceFilter(field_name='color__name', lookup_expr='iexact', choices=COLORS,
                                        empty_label="Все Цвета", label="Цвет двери",
                                        widget=forms.Select(attrs={'class': 'form-control'}))
    brand = django_filters.ModelChoiceFilter(field_name='product__brand__name', queryset=Brand.objects.all(),
                                             empty_label="Все Бренды", label="Бренды ",
                                             widget=forms.Select(attrs={'class': 'form-control'}))
    type = django_filters.ChoiceFilter(field_name='type__type', empty_label="Все", lookup_expr='iexact', choices=TYPES,
                                       label="Тип двери ",
                                       widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Variants
        fields = ['title', 'ordering', 'color', 'brand', 'type']

    def filter_by_order(self, queryset, name, value):
        if value == 'ascending':
            expression = 'title'
        elif value == 'descending':
            expression = '-title'
        elif value == 'price_low_to_high':
            expression = 'sale_price'
        else:
            expression = '-sale_price'
        return queryset.order_by(expression)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class IronVariantsFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains', label="Название двери:",
                                      widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Прим...'}))
    ordering = django_filters.ChoiceFilter(label="Порядок", choices=CHOICES,
                                           method='filter_by_order', null_value='ascending',
                                           empty_label="От А до Я",
                                           widget=forms.Select(attrs={'class': 'form-control'}))
    min_price = django_filters.NumberFilter(field_name='sale_price', lookup_expr='gte', label='Мин. цена',
                                            widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'number',
                                                                          'placeholder': int(
                                                                              Variants.objects.all().order_by(
                                                                                  'sale_price').first().sale_price)}))
    max_price = django_filters.NumberFilter(field_name='sale_price', lookup_expr='lte', label='Макс. цена',
                                            widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'number',
                                                                          'placeholder': int(
                                                                              Variants.objects.all().order_by(
                                                                                  '-sale_price').first().sale_price)}))
    color = django_filters.ChoiceFilter(field_name='color__name', lookup_expr='iexact', choices=COLORS,
                                        empty_label="Все Цвета", label="Цвет двери",
                                        widget=forms.Select(attrs={'class': 'form-control'}))
    brand = django_filters.ModelChoiceFilter(field_name='product__brand__name', queryset=Brand.objects.all(),
                                             empty_label="Все Бренды", label="Бренды ",
                                             widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Variants
        fields = ['title', 'ordering', 'color', 'brand']

    def filter_by_order(self, queryset, name, value):
        if value == 'ascending':
            expression = 'title'
        elif value == 'descending':
            expression = '-title'
        elif value == 'price_low_to_high':
            expression = 'sale_price'
        else:
            expression = '-sale_price'
        return queryset.order_by(expression)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
