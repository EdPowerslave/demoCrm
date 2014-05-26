# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='birth_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='customer',
            name='country',
            field=models.CharField(max_length=b'50', verbose_name=b'country'),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='meetingProject',
            field=models.CharField(max_length=b'30', verbose_name=b'meeting project'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='city',
            field=models.CharField(max_length=b'50', verbose_name=b'city'),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='meetingType',
            field=models.CharField(max_length=b'20', verbose_name=b'meeting type'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='mobilePhone',
            field=models.IntegerField(verbose_name=b'mobile phone '),
        ),
        migrations.AlterField(
            model_name='customer',
            name='homePhone',
            field=models.IntegerField(verbose_name=b'home phone'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.CharField(max_length=b'100', verbose_name=b'address'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='surname',
            field=models.CharField(max_length=b'50', verbose_name=b'surname'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=70, unique=True, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(max_length=b'50', verbose_name=b'name'),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='meetingComment',
            field=models.CharField(max_length=b'50', verbose_name=b'meeting comments'),
        ),
    ]
