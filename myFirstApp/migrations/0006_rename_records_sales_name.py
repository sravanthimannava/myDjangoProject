# Generated by Django 3.2.3 on 2021-06-19 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myFirstApp', '0005_vehicle_types'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sales',
            old_name='records',
            new_name='name',
        ),
    ]
