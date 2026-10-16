from django.contrib import admin
from .models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ("title", "created", "updated", "is_active")
    list_filter = ("is_active",)
    search_fields = ("title", "description")