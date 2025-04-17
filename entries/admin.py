from django.contrib import admin

from entries.models import Entry


class EntryAdmin(admin.ModelAdmin):
    list_display = ('author', 'construction', 'created_at')
    search_fields = ('author__username', 'content')
    list_filter = ('construction', 'created_at')

admin.site.register(Entry, EntryAdmin)
