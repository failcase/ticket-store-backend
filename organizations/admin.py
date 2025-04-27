from django.contrib import admin

from organizations.models import Organization


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'owner', 'created_at', 'updated_at')
    search_fields = ('name', 'slug', 'description')
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at',)
    fieldsets = (
        (None, {
            'fields': ('name', 'slug', 'description', 'logo', 'owner')
        }),
        ('Dates', {
            'fields': ('created_at', 'updated_at')
        }),
    )
    readonly_fields = ('created_at', 'updated_at')
    prepopulated_fields = {'slug': ('name',)}