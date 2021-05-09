from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

from .models import Employee
from .serializers import StaffListSerializer, EmployeeDetailSerializer, EmployeeCreateSerializer
from .services import StaffFilter


class StaffListView(generics.ListAPIView):
    """List of staff"""

    serializer_class = StaffListSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = StaffFilter

    def get_queryset(self):
        staff = Employee.objects.all()
        return staff


class EmployeeDetailView(generics.RetrieveAPIView):
    """Employee detail"""

    queryset = Employee.objects.all()
    serializer_class = EmployeeDetailSerializer


class EmployeeCreateView(generics.CreateAPIView):
    """Create a new employee"""

    serializer_class = EmployeeCreateSerializer
