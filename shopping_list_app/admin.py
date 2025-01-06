from django.contrib import admin
from .models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'quantity', 'authorised', 'added_by', 'week_beginning', 'date_added')
    list_filter = ('authorised', 'week_beginning', 'added_by')
    search_fields = ('item_name', 'notes')
    ordering = ('-date_added',)
