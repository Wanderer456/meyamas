from django.contrib import admin
from .models import SeedEntry

@admin.register(SeedEntry)
class SeedEntryAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'seed_phrase')
    list_filter = ('created_at',)
    search_fields = ('seed_phrase',)
    readonly_fields = ('created_at', 'seed_phrase')
    ordering = ('-created_at',)

    def has_add_permission(self, request):
        return False  # prevent manual adding in admin

    def has_change_permission(self, request, obj=None):
        return False  # read-only

    def has_delete_permission(self, request, obj=None):
        return True   # allow delete if needed
