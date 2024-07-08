from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Organisation
from .serializers import OrganisationSerializer, AddUserToOrganisationSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Organisation, User



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



class AddUserToOrganisation(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, org_id):
        serializer = AddUserToOrganisationSerializer(data=request.data)
        if serializer.is_valid():
            user_id = serializer.validated_data['user_id']
            organisation = get_object_or_404(Organisation, pk=org_id)

            try:
                user = User.objects.get(pk=user_id)
            except User.DoesNotExist:
                return Response(
                    {"error": "User not found"},
                    status=status.HTTP_404_NOT_FOUND
                )

            # Add user to organisation
            organisation.users.add(user)
            organisation.save()

            return Response(
                {"status": "success", "message": "User added to organisation successfully"},
                status=status.HTTP_200_OK
            )

        return Response(
            {"status": "Bad Request", "message": "Client error", "statusCode": 400},
            status=status.HTTP_400_BAD_REQUEST
        )