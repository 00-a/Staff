from rest_framework import serializers

from .models import Employee


class RecursiveSerializer(serializers.Serializer):
    """Recursive for employee children"""

    def to_representation(self, instance):
        serializer = self.parent.parent.__class__(instance, context=self.context)
        return serializer.data


class StaffListSerializer(serializers.ModelSerializer):
    """List of staff"""

    children = RecursiveSerializer(many=True)

    class Meta:
        model = Employee
        fields = '__all__'


class EmployeeCreateSerializer(serializers.ModelSerializer):
    """Create a new employee"""

    class Meta:
        model = Employee
        fields = '__all__'
