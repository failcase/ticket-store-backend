from rest_framework import viewsets, permissions
import django_filters

from organizations.models import Organization
from organizations.serializers import OrganizationSerializer


class OwnerFilter(django_filters.FilterSet):
    """
    Custom filter to filter organizations by owner.
    """

    owner = django_filters.CharFilter(field_name='owner__username', lookup_expr='exact')

    class Meta:
        model = Organization
        fields = ['owner']


class OrganizationViewSet(viewsets.ModelViewSet):
    """
    ViewSet for the Organization model.
    """
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['owner']
    filterset_class = OwnerFilter
    search_fields = ['name', 'slug', 'description']
    lookup_field = 'slug'

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAuthenticated()]
        elif self.request.method in ['PUT', 'PATCH', 'DELETE']:
            # Only the owner of the organization can edit or delete it
            return [permissions.IsAuthenticated(), IsOwner()]
        return [permissions.AllowAny()]

    def perform_create(self, serializer):
        """
        Override the perform_create method to set the owner of the organization
        to the current user.
        """
        serializer.save(owner=self.request.user)


class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an organization to edit or delete it.
    """

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
