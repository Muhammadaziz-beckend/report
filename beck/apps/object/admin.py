from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Object


@admin.register(Object)
class ObjectAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "campania",
        "creator",
    )

    list_display_links = (
        "id",
        "name",
        "campania",
        "creator",
    )

    list_filter = (
        "create_dt",
        "campania",
        "creator",
    )
