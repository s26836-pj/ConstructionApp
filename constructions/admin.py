from django.contrib import admin

from constructions.models import Construction


class ConstructionAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'working_hours', 'is_archived')
    search_fields = ('name', 'location')
    list_filter = ('is_archived',)

admin.site.register(Construction, ConstructionAdmin)
