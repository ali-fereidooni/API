from django.contrib import admin
from .models import User, OtpCode
from .forms import UserCreationForm, UserChangeForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserAdmin(BaseUserAdmin):
    form = UserCreationForm
    add_form = UserChangeForm

    list_display = ('email', 'phone_number', 'is_admin')
    list_filter = ('is_admin',)
    readonly_fields = ('last_login',)
    fieldsets = (
        ('Main', {'fields': ('email', 'phone_number', 'full_name', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_admin',
         'is_superuser', 'last_login', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {'fields': ('email', 'phone_number',
         'full_name', 'password1', 'password2')}),
    )
    search_fields = ('email', 'full_name')
    ordering = ('full_name',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)


@admin.register(OtpCode)
class OtpCodeAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'code', 'created')
