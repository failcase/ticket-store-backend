from rest_framework import serializers

from organizations.models import Organization


class OrganizationSerializer(serializers.ModelSerializer):
    """
    Serializer for the Organization model.
    """

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Organization
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at', 'owner')
