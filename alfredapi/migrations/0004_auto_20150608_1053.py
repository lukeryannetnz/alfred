# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('alfredapi', '0003_auto_20150524_0904'),
    ]

    operations = [
        migrations.AddField(
            model_name='onoffswitch',
            name='description',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AlterField(
            model_name='onoffswitch',
            name='dateAddedUtc',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'Date added'),
        ),
    ]
