# Generated by Django 4.1.4 on 2022-12-20 14:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('input', '0005_alter_applicationinstance_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='DayApplied',
            field=models.DateField(default=datetime.date(2022, 12, 20)),
        ),
    ]
