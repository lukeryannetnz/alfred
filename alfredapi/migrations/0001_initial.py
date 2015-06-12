# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(default=b'', max_length=200)),
                ('dateAddedUtc', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'Date added')),
                ('location', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='OnOffSwitch',
            fields=[
                ('device_ptr', models.OneToOneField(auto_created=True, parent_link=True, primary_key=True, serialize=False, to='alfredapi.Device')),
                ('gpioPinBcmIndex', models.IntegerField(default=4)),
            ],
            bases=('alfredapi.device',),
        ),
    ]
