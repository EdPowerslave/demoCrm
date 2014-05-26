# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0012_auto_20140520_0328'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meeting',
            old_name='meetingDate',
            new_name='meeting_date',
        ),
        migrations.RenameField(
            model_name='meeting',
            old_name='meetingProject',
            new_name='meeting_project',
        ),
        migrations.AddField(
            model_name='meeting',
            name='meeting_type',
            field=models.CharField(default=b'Ziyaret', max_length=b'20', choices=[(b'Ziyaret', b'Ziyaret'), (b'Telefon(Arad\xc4\xb1)', b'Telefon(Arad\xc4\xb1)'), (b'Telefon(Biz Arad\xc4\xb1k)', b'Telefon(Biz Arad\xc4\xb1k)')]),
            preserve_default=True,
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='homePhone',
            new_name='home_phone',
        ),
        migrations.RenameField(
            model_name='meeting',
            old_name='meetingComment',
            new_name='meeting_comment',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='mobilePhone',
            new_name='mobile_phone',
        ),
        migrations.RemoveField(
            model_name='meeting',
            name='meetingType',
        ),
    ]
