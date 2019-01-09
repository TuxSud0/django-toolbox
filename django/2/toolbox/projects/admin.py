from django.contrib import admin
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','number', 'client', 'location')
    list_filter = ('name','number', 'client', 'location')
    readonly_fields = ('username','submitted',)
    fieldsets = (
        ('Project Information', {
            'fields': ('name','number', 'client', 'location')
        }),

		)

admin.site.register(Project, ProjectAdmin)