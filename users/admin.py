from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class UserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_superuser')
    list_filter = ('is_superuser',)
    search_fields = ('username', 'email')
    ordering = ('date_joined',)
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Permissões', {'fields': ('is_superuser',)}),
        ('Datas importantes', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_superuser')}
        ),
    )

admin.site.register(User, UserAdmin)
