# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-23 19:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conf', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='conf',
            name='i18n_timezone',
            field=models.CharField(default='America/New_York', max_length=255, verbose_name='Timezone'),
        ),
    ]
