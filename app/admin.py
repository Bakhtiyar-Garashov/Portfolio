from django.contrib import admin
from .models import Project, File


# Register your models here.

class Projectadmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'type']
    list_display_links = ['name', 'created_at']
    list_filter = ['type', 'created_at']
    search_fields = ['name']

    class Meta:
        model = Project


class Fileadmin(admin.ModelAdmin):
    list_display = ['project', 'file_name', 'file']
    list_display_links = ['project', 'file_name', 'file']
    list_filter = ['file_name']
    search_fields = ['file_name']

    class Meta:
        model = File


admin.site.register(Project, Projectadmin)
admin.site.register(File, Fileadmin)
