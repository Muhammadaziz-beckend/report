from django.db import models

from utils.models import DataTimeCUAbstract


class Report(DataTimeCUAbstract):

    MINUS = "minus"
    ADD = "add"

    TYPE_REPO = (
        (MINUS, "отнять"),
        (ADD, "прибавить"),
    )

    title = models.CharField(
        "Названия",
        max_length=85,
    )
    type_repo = models.CharField(
        "Тиа операции",
        choices=TYPE_REPO,
        max_length=5,
    )
    owner = models.ForeignKey(
        "account.User",
        models.SET_NULL,
        null=True,
        verbose_name="Владелиц",
    )
    amoute = models.DecimalField(
        "Сумма",
        max_digits=10,
        decimal_places=2,
        # default=0
    )
    old_amoute = models.DecimalField(
        "Сумма",
        max_digits=10,
        decimal_places=2,
        default=0,
    )
    campania = models.ForeignKey(
        "campania.Campania",
        models.CASCADE,
        related_name="reports",
        verbose_name="Компания",
    )
    _object = models.ForeignKey(
        "object.Object",
        models.CASCADE,
        related_name="reports",
        verbose_name="Объект",
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "отчет"
        verbose_name_plural = "отчеты"
