from django.db import models
from .abstract import TimeStampedUUIDModel
from django.utils.translation import gettext_lazy as _


class Workcalendar(TimeStampedUUIDModel):
    date = models.DateField(
        blank=True,
        null=True,
        verbose_name=_('Date'),
        help_text=_('Date in the year'))
    holiday = models.BooleanField(
        blank=True,
        null=True,
        unique=False,
        default=False,
        verbose_name=_("Holiday"),
        help_text=_("True if it is holiday, False if it is not holiday")
    )

