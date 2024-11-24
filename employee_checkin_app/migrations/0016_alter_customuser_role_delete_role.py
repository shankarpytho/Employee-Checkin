# Generated by Django 5.1.3 on 2024-11-24 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_checkin_app', '0015_alter_customuser_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('admin', 'Admin'), ('employee', 'Employee')], default='employee', max_length=20),
        ),
        migrations.DeleteModel(
            name='Role',
        ),
    ]
