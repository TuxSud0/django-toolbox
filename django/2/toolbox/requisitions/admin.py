from django.contrib import admin
from .models import Requisitions

class RequisitionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'number','name')
    list_filter = ('id', 'number','name')
    fieldsets = (
        ('Requisitions', {
            'fields': ('number','name',)
        }),

		)

admin.site.register(Requisitions, RequisitionsAdmin)
