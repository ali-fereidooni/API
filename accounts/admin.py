from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserAdmin(BaseUserAdmin):
    list_display = (
        "phone", "first_name",
        "last_name", "is_staff",
        "author",
    )
    list_filter = (
        "is_staff", "is_superuser",
        "groups",
    )
    search_fields = (
        "first_name", "last_name",
        "phone",
    )
    ordering = (
        "-is_superuser", "-is_staff",
        "-pk",
    )
    list_per_page = 25


admin.site.register(User, UserAdmin)
