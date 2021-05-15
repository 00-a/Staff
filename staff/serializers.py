from rest_framework import serializers

from .models import Employee


class RecursiveSerializer(serializers.Serializer):
    """Recursive for employee children"""

    def to_representation(self, data):
        serializer = self.parent.parent.__class__(data, context=self.context)
        return serializer.data


class StaffListSerializer(serializers.ModelSerializer):
    """List of staff"""

    position = serializers.SlugRelatedField(slug_field="name", read_only=True)
    children = RecursiveSerializer(many=True)

    class Meta:
        model = Employee
        fields = '__all__'


class ChildrenEmployeeDetailSerializer(serializers.ModelSerializer):
    """Serializer for employee children in detail view"""

    class Meta:
        model = Employee
        fields = ('name', 'surname')


class EmployeeDetailSerializer(serializers.ModelSerializer):
    """Details of employee"""

    position = serializers.SlugRelatedField(slug_field="name", read_only=True)
    parent = serializers.SlugRelatedField(slug_field="name", read_only=True)
    children = ChildrenEmployeeDetailSerializer(many=True)

    class Meta:
        model = Employee
        fields = '__all__'


class EmployeeCreateSerializer(serializers.ModelSerializer):
    """Create a new employee"""

    class Meta:
        model = Employee
        fields = '__all__'
