# Generated by Django 4.0 on 2023-10-16 13:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('parameters', '0003_alter_parameter_enabled_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parameter',
            name='ValidityEndDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 15, 13, 42, 13, 654150, tzinfo=utc)),
        ),
    ]