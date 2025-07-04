from django.db import models
from django.contrib.auth.models import AbstractUser
from django_resized import ResizedImageField
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
from .manager import UserNewManager


class User(AbstractUser):
    ADMIN = "admin"
    EMPLOYEE = "employee"

    ROLE = (
        (ADMIN, _("Админ")),
        (EMPLOYEE, _("сотрудник")),
    )

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"
        ordering = ("-date_joined",)

    username = None
    avatar = ResizedImageField(
        _("аватарка"),
        size=[500, 500],
        crop=["middle", "center"],
        upload_to="avatars/",
        force_format="WEBP",
        quality=90,
        null=True,
        blank=True,
    )
    phone = PhoneNumberField(
        _("номер телефона"),
        unique=True,
    )
    first_name = models.CharField(
        _("first name"),
        max_length=150,
    )
    last_name = models.CharField(
        _("last name"),
        max_length=150,
    )
    email = models.EmailField(
        _("email address"),
        blank=True,
        null=True,
    )
    role = models.CharField(
        "роль",
        choices=ROLE,
        default=EMPLOYEE,
        max_length=15,
    )
    campania = models.ForeignKey(
        "campania.Campania",
        models.CASCADE,
        related_name="users",
        blank=True,
        null=True,
        verbose_name="Компания",
    )

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = []

    objects = UserNewManager()

    @property
    def get_full_name(self):
        return f"{self.last_name} {self.first_name}"

    get_full_name.fget.short_description = _("полное имя")

    def __str__(self):
        return f"{str(self.phone)}-{self.get_full_name}"
