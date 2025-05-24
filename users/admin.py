from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    """Admin configuration for CustomUser model"""
    
    # Fields to display in the list view
    list_display = ('email', 'name', 'is_staff')
    
    # Fields to search by
    search_fields = ('email', 'name')
    
    # Fields to filter by
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    
    # Fields to display in the detail view
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('name',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    
    # Fields to add in the add form
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2'),
        }),
    )
    
    # Ordering
    ordering = ('email',)
    
    # Fields that can be edited in the list view
    list_editable = ('is_staff',)
