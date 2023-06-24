import logging
from django.db import models
from django.utils.translation import gettext_lazy as _


class Classroom(models.Model):
    classroom_year = models.IntegerField(
        blank=True,
        null=True,
        verbose_name=_("classroom_year"),
        help_text=_("Year in the current stage"))

    classroom_line = models.CharField(
        max_length=1,
        blank=True,
        null=True,
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
        verbose_name=_("Stage"),
        help_text=_("Stage of the classroom"))

    def __str__(self):
        return f"{self.classroom_year}º {self.classroom_line} {self.stage}"
