from django.contrib import admin
from .models import Definition, Package

class DefinitionAdmin(admin.ModelAdmin):
    list_display = ('tag','desc','wbs','pkg','est_group','bat_lim','pid','pfd','eq_class')
    list_filter = ('tag','pkg','est_group','bat_lim','eq_class')
    

	
class PackageAdmin(admin.ModelAdmin):
    list_display = ('number','name')
    list_filter = ('number','name')

	
	
admin.site.register(Definition, DefinitionAdmin)
admin.site.register(Package, PackageAdmin)

'''    ### make fieldset for various equipment list views
fieldsets = (
        ('Equipment', {
            'fields': ('tag','name',)
            
        })
    )
	
	#readonly_fields = ('username','submitted',)
'''
