from rest_framework import serializers

from .models import Employee


class StaffListSerializer(serializers.ModelSerializer):
    """List of staff"""

    parent = serializers.SlugRelatedField(read_only=True, slug_field='name')
    position = serializers.SlugRelatedField(read_only=True, slug_field='name')

    class Meta:
        model = Employee
        fields = '__all__'


class EmployeeCreateSerializer(serializers.ModelSerializer):
    """List of staff"""

    class Meta:
        model = Employee
        fields = '__all__'
