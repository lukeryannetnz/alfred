# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OnOffSwitchAdapter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('location', models.CharField(max_length=200)),
                ('gpioPinBcmIndex', models.IntegerField(default=4)),
                ('dateAddedUtc', models.DateTimeField(verbose_name=b'Date added')),
            ],
        ),
    ]
