# Generated by Django 4.1 on 2022-10-18 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('convertion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordonnance',
            name='nbr_med',
            field=models.IntegerField(null=True, verbose_name=20),
        ),
    ]
