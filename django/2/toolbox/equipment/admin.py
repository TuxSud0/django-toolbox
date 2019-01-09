from django.contrib import admin
from .models import Equipment

class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag','name')
    list_filter = ('id', 'tag','name')
    readonly_fields = ('username','submitted',)
    fieldsets = (
        ('Equipment', {
            'fields': ('tag','name',)
        }),

		)

admin.site.register(Equipment, EquipmentAdmin)