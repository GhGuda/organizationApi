from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Organisation
from .serializers import OrganisationSerializer

class OrganisationListAPI(generics.ListCreateAPIView):
    queryset = Organisation.objects.all()
    serializer_class = OrganisationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.request.user.organisations.all()

class OrganisationDetailAPI(generics.RetrieveAPIView):
    queryset = Organisation.objects.all()
    serializer_class = OrganisationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.request.user.organisations.all()

