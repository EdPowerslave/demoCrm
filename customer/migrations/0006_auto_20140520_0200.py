# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_auto_20140520_0144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='meetingProject',
            field=models.CharField(max_length=b'30', null=True, verbose_name=b'meeting project'),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='meetingComment',
            field=models.CharField(max_length=b'50', null=True, verbose_name=b'meeting comments'),
        ),
    ]
