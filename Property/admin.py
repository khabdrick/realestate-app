from django.contrib import admin

from .models import Properties

class PropertyAdmin(admin.ModelAdmin):
	list_display		= ['__str__', 'agent', 'property_type', 'price', 'timestamp']
	search_fields		= ['agent', 'property_type', 'price', 'timestamp']

admin.site.register(Properties)