from rest_framework import serializers
from .models import Organisation

class OrganisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organisation
        fields = ['orgId', 'name', 'description']


class AddUserToOrganisationSerializer(serializers.Serializer):
    user_id = serializers.CharField(required=True)