# Generated by Django 3.2.3 on 2021-06-21 03:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myFirstApp', '0007_alter_sales_company'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Sales',
        ),
        migrations.DeleteModel(
            name='Vehicle',
        ),
    ]
