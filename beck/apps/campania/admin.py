from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import *


@admin.register(Campania)
class CampaniaAdmin(ModelAdmin):

    list_display = (
        "id",
        "name",
        "amount_money",
        "owner",
        "create_dt",
    )

    list_display_links = (
        "id",
        "name",
        "amount_money",
        "owner",
        "create_dt",
    )

    list_filter = ("create_dt",)

    readonly_fields = ("amount_money",)
