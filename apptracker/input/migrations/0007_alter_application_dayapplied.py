# Generated by Django 4.1.4 on 2022-12-20 14:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('input', '0006_application_dayapplied'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='DayApplied',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]