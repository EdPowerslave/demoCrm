# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0011_auto_20140520_0212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='meetingProject',
            field=models.CharField(default=b'YT Residence', max_length=b'20', choices=[(b'YT Residence', b'YT Residence'), (b'YT Life', b'YT Life')]),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='meetingType',
            field=models.CharField(default=b'Ziyaret', max_length=b'20', choices=[(b'Ziyaret', b'Ziyaret'), (b'Telefon', b'Telefon')]),
        ),
    ]
