# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('alfredapp', '0002_auto_20150524_0826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onoffswitch',
            name='dateAddedUtc',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name=b'Date added'),
        ),
    ]
