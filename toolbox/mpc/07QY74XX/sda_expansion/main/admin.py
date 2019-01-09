from django.contrib import admin
from .models import Definition, Package

class DefinitionAdmin(admin.ModelAdmin):
    list_display = ('tag','desc','wbs')
    list_filter = ('tag','desc','wbs')
    

	
class PackageAdmin(admin.ModelAdmin):
    list_display = ('number','name')
    list_filter = ('number','name')

	
	
admin.site.register(Definition, DefinitionAdmin)
admin.site.register(Package, PackageAdmin)

'''    
fieldsets = (
        ('Equipment', {
            'fields': ('tag','name',)
            
        })
    )
	
	#readonly_fields = ('username','submitted',)
'''
