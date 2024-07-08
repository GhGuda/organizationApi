from django.contrib import admin

# Register your models here.
from users.models import UserManager, User


admin.site.register(User)
# admin.site.register(UserManager)