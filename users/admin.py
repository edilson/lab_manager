from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

from .models import User

class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'email', 'created', 'modified')
    list_filter = ('is_active', 'is_staff')
    search_fields = ('email',)
    ordering = ('name',)
    filter_horizontal = ('groups', 'user_permissions',)

    fieldsets = (
        (None, {'fields': ('email', 'name', 'password',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2')
        }),
    )

admin.site.register(User, CustomUserAdmin)