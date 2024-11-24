# Generated by Django 5.1.3 on 2024-11-24 11:43

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_checkin_app', '0016_alter_customuser_role_delete_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkindetails',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='checkindetails',
            name='employee_name',
        ),
        migrations.RemoveField(
            model_name='checkindetails',
            name='modified_by',
        ),
        migrations.AlterField(
            model_name='checkindetails',
            name='checkin_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='checkindetails',
            name='checkout_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='checkindetails',
            name='location',
            field=models.CharField(default='chennai', max_length=255),
        ),
        migrations.AlterField(
            model_name='checkindetails',
            name='modified',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
