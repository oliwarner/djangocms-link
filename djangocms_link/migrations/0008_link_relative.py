# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_link', '0007_set_related_name_for_cmsplugin_ptr'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='relative',
            field=models.CharField(blank=True, verbose_name='relative', max_length=2048, null=True, help_text='A relative link has priority over a text link'),
        ),
    ]
