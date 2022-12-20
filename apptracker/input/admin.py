from django.contrib import admin

# Register your models here.
from .models import Application


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('CompanyName', 'DayApplied', 'ApplicationStatus', 'Pay', 'TermLength', 'Position')
    list_filter = ('CompanyName', 'ApplicationStatus', 'Pay', 'TermLength')

