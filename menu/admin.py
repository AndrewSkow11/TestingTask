from django.contrib import admin
from .models import MenuItem

# Register your models here.

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent')
    list_filter = ('parent',)

admin.site.register(MenuItem, MenuItemAdmin)