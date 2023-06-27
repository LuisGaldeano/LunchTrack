import logging
from django.db import models
from .abstract import TimeStampedUUIDModel
from django.utils.translation import gettext_lazy as _


class Classroom(TimeStampedUUIDModel):
    classroom_year = models.IntegerField(
        blank=True,
        null=True,
        unique=False,
        verbose_name=_("classroom_year"),
        help_text=_("Year in the current stage"))

    classroom_line = models.CharField(
        max_length=1,
        blank=True,
        null=True,
        unique=False,
        verbose_name=_("classroom_line"),
        help_text=_("Line in the current year"))

    options = (
        ("Infant", "Infant"),
        ("Primary", "Primary"),
        ("Secondary", "Secondary")
    )
    stage = models.CharField(
        max_length=20,
        choices=options,
        blank=True,
        null=True,
        unique=False,
        verbose_name=_("Stage"),
        help_text=_("Stage of the classroom"))

    class Meta:
        verbose_name = _('Classroom')
        verbose_name_plural = _('Classrooms')

        unique_together = ('classroom_year', 'classroom_line', 'stage')

    def __str__(self):
        return f"{self.classroom_year}º {self.classroom_line} {self.stage}"
