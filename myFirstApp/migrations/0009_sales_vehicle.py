# Generated by Django 3.2.3 on 2021-06-21 04:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('myFirstApp', '0008_auto_20210621_0927'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=200)),
                ('year', models.CharField(max_length=4)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='myFirstApp.vehicle')),
            ],
        ),
    ]
