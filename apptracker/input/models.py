import django
from django.db import models
from django.urls import reverse
from datetime import date
import uuid

# Create your models here.
ApplicationStatusChoices = [
    ('Applied', 'Applied'),
    ('Selected', 'Selected'),
    ('Rejected', 'Rejected'),
    ('Interviewing', 'Interviewing'),
]

TermLengthChoices = [
    ('Spring', 'Spring'),
    ('Fall', 'Fall'),
    ('Winter', 'Winter'),
    ('Summer', 'Summer'),
]


class Application(models.Model):
    CompanyName = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        verbose_name='Company Name',
    )
    DayApplied = models.DateField(
        default=django.utils.timezone.now,
        verbose_name='Day Applied',
    )
    ApplicationStatus = models.CharField(
        max_length=100,
        choices=ApplicationStatusChoices,
        default='Applied',
        blank=False,
        verbose_name='Application Status',
    )
    TermLength = models.CharField(
        max_length=100,
        choices=TermLengthChoices,
        blank=True,
        verbose_name='Term Length',
    )
    Pay = models.IntegerField(
        blank=True,
        verbose_name='Pay',
    )
    Position = models.CharField(
        max_length=100,
        blank=False,
        verbose_name='Position',
    )

    # ID = models.UUIDField(primary_key=True, default=uuid.uuid4,
    # help_text='Unique ID')

    def __str__(self):
        """String for representing the Model object."""
        return self.CompanyName

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this book."""
        return reverse('application-detail', args=[str(self.id)])
