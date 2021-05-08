from rest_framework import serializers

from .models import Employee


class StaffSerializer(serializers.ModelSerializer):
    """List of staff"""

    class Meta:
        model = Employee
        fields = '__all__'
