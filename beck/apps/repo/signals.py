from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import *


@receiver(post_save, sender=Report)
def report_handler(sender, instance: Report, created, **kwargs):

    owner_campania = instance.owner.campania

    if owner_campania and instance.campania != owner_campania:

        Report.objects.filter(pk=instance.pk).update(
            campania=owner_campania,
        )

    if instance.amoute and instance.old_amoute != instance.amoute:

        campania = instance.campania

        if instance.type_repo == instance.ADD:
            campania.amount_money -= instance.old_amoute
            campania.amount_money += instance.amoute
        else:
            campania.amount_money += instance.old_amoute
            campania.amount_money -= instance.amoute

        Report.objects.filter(pk=instance.pk).update(
            old_amoute=instance.amoute,
        )

        campania.save()


@receiver(post_delete, sender=Report)
def report_delete_handel(sender, instance: Report, *args, **kwargs):

    if instance.type_repo == instance.ADD:
        instance.campania.amount_money -= instance.amoute
    else:
        instance.campania.amount_money += instance.amoute

    instance.campania.save()
