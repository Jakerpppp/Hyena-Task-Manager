# Generated by Django 4.2.6 on 2023-11-29 14:20

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0012_alter_task_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(validators=[django.core.validators.MinValueValidator(limit_value=datetime.datetime(2023, 11, 29, 14, 20, 35, 968017, tzinfo=datetime.timezone.utc))]),
        ),
    ]
