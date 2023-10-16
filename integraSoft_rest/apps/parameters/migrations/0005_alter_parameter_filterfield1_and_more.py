# Generated by Django 4.0 on 2023-10-16 14:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('parameters', '0004_alter_parameter_validityenddate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parameter',
            name='FilterField1',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='parameter',
            name='FilterField2',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='parameter',
            name='FilterField3',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='parameter',
            name='ValidityEndDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 15, 14, 43, 45, 391062, tzinfo=utc)),
        ),
    ]