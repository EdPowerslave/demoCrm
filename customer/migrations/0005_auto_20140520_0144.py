# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_auto_20140520_0053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='meetingType',
            field=models.CharField(default=b'ZT', max_length=b'2', choices=[(b'ZT', b'Ziyaret'), (b'TF', b'Telefon')]),
        ),
    ]
