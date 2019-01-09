from django.contrib import admin
from .models import equip, reqpkg

class equipAdmin(admin.ModelAdmin):
	list_display = ('tag_no','name')

class reqpkgAdmin(admin.ModelAdmin):
	list_display = ('pkg_no','pkg_name')

admin.site.register(reqpkg, reqpkgAdmin)
admin.site.register(equip,equipAdmin)
# Register your models here.
