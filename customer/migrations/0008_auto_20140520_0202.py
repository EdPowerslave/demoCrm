# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0007_auto_20140520_0201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='meetingComment',
            field=models.TextField(max_length=b'50', verbose_name=b'meeting comments'),
        ),
    ]
