# Generated by Django 3.2.18 on 2023-03-05 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0002_booking_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='date_start',
            new_name='check_in',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='date_end',
            new_name='check_out',
        ),
    ]
