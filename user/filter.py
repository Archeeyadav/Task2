import django_filters
from django.db.models import Q
from .models import CarListing, Product, Contact

class CarListingFilter(django_filters.FilterSet):
    # looking_for = django_filters.CharFilter(lookup_expr='icontains')
    keywords = django_filters.CharFilter(method='filter_keywords')

    class Meta:
        model = CarListing
        fields = {
            'specifications': ['exact', 'icontains'],
            'category': ['exact', 'icontains'],
            'car_type': ['exact', 'icontains'],
        }
    
    
    def filter_keywords(self, queryset, name, value):
        words = value.split()
        filters = Q()

        exact_match_filter = Q(looking_for__icontains=value)
        exact_match_results = queryset.filter(exact_match_filter)

        if exact_match_results.exists():
            return exact_match_results
            
        else:
            for word in words:
                filters |= Q(looking_for__icontains=word)

            if filters:
                return queryset.filter(filters)
            else:
                return queryset


class ProductFilter(django_filters.FilterSet):

    class Meta:
        model = Product
        fields = {
            'name': ['exact', 'icontains'],
        }
    
     
class ContactFilter(django_filters.FilterSet):

    class Meta:
        model = Contact
        fields = {
            'user': ['exact'],
        }
    
     