# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-12 08:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_portfolio'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='on_services',
            field=models.BooleanField(default=False, verbose_name='Показывать на странице услуг'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='on_main',
            field=models.BooleanField(default=False, verbose_name='Показывать на главной'),
        ),
    ]
