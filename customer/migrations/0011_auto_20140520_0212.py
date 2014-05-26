# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0010_auto_20140520_0203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='meetingProject',
            field=models.CharField(default=b'YR', max_length=b'2', choices=[(b'YR', b'YT Residence'), (b'YL', b'YT Life')]),
        ),
    ]
