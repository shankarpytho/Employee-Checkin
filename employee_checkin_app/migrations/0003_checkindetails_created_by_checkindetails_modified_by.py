# Generated by Django 5.1.3 on 2024-11-17 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_checkin_app', '0002_remove_checkindetails_checkout_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkindetails',
            name='created_by',
            field=models.CharField(default='sri', max_length=255),
        ),
        migrations.AddField(
            model_name='checkindetails',
            name='modified_by',
            field=models.CharField(default='sri', max_length=255),
        ),
    ]