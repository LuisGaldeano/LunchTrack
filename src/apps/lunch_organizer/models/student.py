import logging
from django.db import models
from .abstract import TimeStampedUUIDModel
from django.utils.translation import gettext_lazy as _
from .classroom import Classroom


class Student(TimeStampedUUIDModel):
    name = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        unique=False,
        verbose_name=_("Name"),
        help_text=_("Name of the student"))

    surname = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        unique=False,
        verbose_name=_("Surname"),
        help_text=_("Surname of the student"))

    allergies = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        unique=False,
        verbose_name=_("Allergies"),
        help_text=_("Allergies of the student"))

    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Student')
        verbose_name_plural = _('Students')

        unique_together = ('name', 'surname')

    def __str__(self):
        return f"{self.name} {self.surname}"
