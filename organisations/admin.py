from django.contrib import admin

# Register your models here.
from organisations.models import Organisation

admin.site.register(Organisation)