from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserChangeForm, UserCreationForm


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'phone', 'is_admin')
    list_filter = ('is_admin',)
    readonly_fields = ('last_login',)

    fieldsets = (
        ('Main', {'fields': ('email', 'phone',
         'first_name', 'last_name', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_admin', 'is_superuser',
         'last_login', 'groups')}),

    )

    add_fieldsets = (
        (None, {'fields': ('phone', 'email',
         'first_name', 'last_name', 'password1', 'password2')}),
    )

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

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser
        if not is_superuser:
            form.base_fields['is_superuser'].disabled = True
        return form


admin.site.register(User, UserAdmin)
