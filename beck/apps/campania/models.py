from django.db import models

from utils.models import DataTimeCUAbstract


class Campania(DataTimeCUAbstract):

    name = models.CharField(
        "Названия",
        max_length=65,
    )
    amount_money = models.DecimalField(
        "Сумма денег",
        max_digits=10,
        decimal_places=2,
        default=0,
    )
    owner = models.OneToOneField(
        "account.User",
        models.CASCADE,
        related_name="campaigns",
        verbose_name="Владелиц",
    )

    
    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"
        
    def __str__(self):
        return self.name
    