from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Report


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "title",
        "owner",
        "type_repo",
        "amoute",
        "campania",
        "_object",
        "create_dt",
    )

    list_display_links = (
        "id",
        "title",
        "owner",
        "type_repo",
        "amoute",
        "campania",
        "_object",
        "create_dt",
    )

    list_filter = (
        "owner",
        "campania",
        "_object",
        "create_dt",
    )

    readonly_fields = (
        'old_amoute',
    )