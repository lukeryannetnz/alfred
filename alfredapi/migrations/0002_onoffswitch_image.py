# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alfredapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='onoffswitch',
            name='image',
            field=models.ImageField(default='', upload_to=b'uploads/%Y/%m/%d/'),
            preserve_default=False,
        ),
    ]
