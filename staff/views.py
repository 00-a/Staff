from rest_framework import generics

from .models import Employee
from .serializers import StaffListSerializer, EmployeeDetailSerializer, EmployeeCreateSerializer


class StaffListView(generics.ListAPIView):
    """List of staff"""

    serializer_class = StaffListSerializer

    def get_queryset(self):
        staff = Employee.objects.all()
        return staff


class EmployeeDetailView(generics.RetrieveAPIView):
    """Employee detail"""

    queryset = Employee.objects.filter()
    serializer_class = EmployeeDetailSerializer


class EmployeeCreateView(generics.CreateAPIView):
    """Create a new employee"""

    serializer_class = EmployeeCreateSerializer

