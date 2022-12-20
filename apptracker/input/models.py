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
    )
    ApplicationStatus = models.CharField(
        max_length=100,
        choices=ApplicationStatusChoices,
        default='Applied',
        blank=False,
    )
    TermLength = models.CharField(
        max_length=100,
        choices=TermLengthChoices,
        blank=True,
    )
    Pay = models.IntegerField(
        blank=True,
    )
    Position = models.CharField(
        max_length=100,
        blank=False,
    )

    def __str__(self):
        """String for representing the Model object."""
        return self.CompanyName

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this book."""
        return reverse('application-detail', args=[str(self.id)])


class ApplicationInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text='Unique ID')
    Application = models.ForeignKey('Application', on_delete=models.RESTRICT, null=True)

    class Meta:
        ordering = ['Application']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.Application.CompanyName})'
