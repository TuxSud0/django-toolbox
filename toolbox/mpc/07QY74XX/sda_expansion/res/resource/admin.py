from django.contrib import admin
from .models import Wbs, Equipment_Type

class WbsAdmin(admin.ModelAdmin):
    list_display = ('code','description','equipment_type')
    list_filter = ('code','description','equipment_type')
    readonly_fields = ('code','description')

class Equipment_TypeAdmin(admin.ModelAdmin):
    list_display = ('type',)
    list_filter = ('type',)

admin.site.register(Wbs,WbsAdmin)
admin.site.register(Equipment_Type,Equipment_TypeAdmin)
