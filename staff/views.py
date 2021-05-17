from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .models import Employee
from .serializers import StaffListSerializer, EmployeeDetailSerializer, EmployeeCreateSerializer
from .services import StaffFilter


class StaffListView(generics.ListAPIView):
    """List of staff"""

    serializer_class = StaffListSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = StaffFilter
    pagination_class = PageNumberPagination
    permission_classes = [IsAdminUser]
    queryset = Employee.objects.filter(parent=None)


class EmployeeDetailView(generics.RetrieveAPIView):
    """Employee detail"""

    queryset = Employee.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = EmployeeDetailSerializer


class EmployeeCreateView(generics.CreateAPIView):
    """Create a new employee"""

    permission_classes = [IsAuthenticated]
    serializer_class = EmployeeCreateSerializer
