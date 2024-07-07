from django.urls import path
from .views import OrganisationListAPI, OrganisationDetailAPI

urlpatterns = [
    path('', OrganisationListAPI.as_view(), name='organisation-list'),
    path('<uuid:org_id>/', OrganisationDetailAPI.as_view(), name='organisation-detail'),
]
