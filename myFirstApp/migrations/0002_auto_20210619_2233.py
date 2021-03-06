# Generated by Django 3.2.3 on 2021-06-19 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myFirstApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='type',
            field=models.CharField(default='Other', max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='title',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=128, unique=True)),
                ('year', models.CharField(max_length=4)),
                ('records', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='myFirstApp.vehicle')),
            ],
        ),
    ]
