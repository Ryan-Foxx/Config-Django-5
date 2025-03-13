from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser

    # list_display = ['username', 'email', 'is_staff']

    # add_fieldsets = UserAdmin.add_fieldsets + (
    #     (None, {'fields': ()}),
    # )
    # fieldsets = UserAdmin.fieldsets + (
    #     (None, {'fields': ()}),
    # )


# admin.site.register(CustomUser, CustomUserAdmin)
