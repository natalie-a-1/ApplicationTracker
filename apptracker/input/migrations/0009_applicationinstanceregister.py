# Generated by Django 4.1.4 on 2022-12-20 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('input', '0008_alter_application_applicationstatus_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationInstanceRegister',
            fields=[
                ('applicationinstance_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='input.applicationinstance')),
            ],
            bases=('input.applicationinstance',),
        ),
    ]
