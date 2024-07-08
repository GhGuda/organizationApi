from django.urls import path
from .views import OrganisationListAPI, OrganisationDetailAPI, AddUserToOrganisation
from users.views import UserDetailAPI

urlpatterns = [
    path('api/organisations', OrganisationListAPI.as_view(), name='organisation-list'),
    path('api/organisations/<uuid:org_id>/', OrganisationDetailAPI.as_view(), name='organisation-detail'),
    path('api/organisations/<str:org_id>/users', AddUserToOrganisation.as_view(), name='add-user-to-organisation'),
    path('api/users/<int:pk>/', UserDetailAPI.as_view(), name='user-detail'),
]
