from django_filters import rest_framework as filters

from staff.models import Employee


class StaffFilter(filters.FilterSet):

    salary = filters.RangeFilter()
    employment_date = filters.RangeFilter()

    class Meta:
        model = Employee
        fields = ('position', 'salary', 'employment_date')
