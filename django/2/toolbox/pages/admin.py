from django.contrib import admin
from .models import Page

# Register your models here.
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'permalink','update_date',)
    #list_filter = ('name','number', 'client', 'location')
    #readonly_fields = ('username','submitted',)
	
    #fieldsets = 
	
admin.site.register(Page, PageAdmin)