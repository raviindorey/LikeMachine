from django.contrib import admin

from .models import LinkPost


@admin.register(LinkPost)
class LinkPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'link')
    search_fields = ('title', 'link')
