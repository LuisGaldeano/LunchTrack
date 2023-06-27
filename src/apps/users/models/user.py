from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .abstract import TimeStampedUUIDModel


class User(AbstractUser, TimeStampedUUIDModel):
    DIRECTION, TEACHER, TEAM_COORDINATOR, DINING_ROOM_STAFF = 'd', 't', 'tc', 'dr'
    ALLOWED_STAFF = (
        (DIRECTION, _('Direction')),
        (TEACHER, _('Teacher')),
        (TEAM_COORDINATOR, _('Team Coordinator')),
        (DINING_ROOM_STAFF, _('Dining Room Staff')),
    )

    username = models.CharField(
        max_length=255,
        unique=True,
        verbose_name=_('Username'),
        help_text=_('Worker Username'),
    )
    email = models.EmailField(
        max_length=255,
        unique=True,
        verbose_name=_('Email'),
        help_text=_('Worker email'),
    )
    name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_('Name'),
        help_text=_('Worker name'),
    )
    last_name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_('Surname'),
        help_text=_('Worker last name'),
    )
    image = models.ImageField(upload_to='perfil/', max_length=255, null=True, blank=True, verbose_name=_('Image'))
    staff = models.CharField(
        max_length=4,
        choices=ALLOWED_STAFF,
        blank=True,
        null=True,
        verbose_name=_('Staff'),
        help_text=_('Position that the worker has in the school, it can be: '
                    'Direction(d), Teacher(t), Team Coordinator(tc),  or Dining Room Staff(dr)'),
    )
    birthdate = models.DateField(
        blank=True,
        null=True,
        verbose_name=_('Birthday'),
        help_text=_('Birthday of the staff'),
    )

    @property
    def age(self):
        return timezone.now().year - self.birthdate.year

    def __str__(self):
        return str(_(f"User {self.username}, with name: {self.name} {self.last_name}"))
