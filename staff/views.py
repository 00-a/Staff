from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Employee
from .serializers import StaffListSerializer, EmployeeCreateSerializer


class StaffListView(APIView):
    """List of staff"""

    def get(self, request):
        staff = Employee.objects.all()
        serializer = StaffListSerializer(staff, many=True)
        return Response(serializer.data)


class EmployeeDetailView(APIView):
    """Employee detail"""

    def get(self, request, pk):
        employee = Employee.objects.get(pk=pk)
        serializer = StaffListSerializer(employee)
        return Response(serializer.data)


class EmployeeCreateView(APIView):
    """Create a new employee"""

    def post(self, request):
        employee = EmployeeCreateSerializer(data=request.data)
        if employee.is_valid():
            employee.save()
        return Response(status=201)
