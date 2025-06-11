from django.db import models

from utils.models import DataTimeCUAbstract


class Object(DataTimeCUAbstract):

    name = models.CharField(
        "Названия",
        max_length=85,
    )
    campania = models.ForeignKey(
        "campania.Campania",
        models.CASCADE,
        related_name="objects",
        verbose_name="Компания",
    )
    creator = models.ForeignKey(
        "account.User",
        models.SET_NULL,
        verbose_name="Создатель",
        null=True,
    )

    class Meta:
        verbose_name = "Объект"
        verbose_name_plural = "Объекты"

    def __str__(self):
        campania = ""

        if self.campania:
            campania = self.campania

        return f"{campania}-{self.name}"
