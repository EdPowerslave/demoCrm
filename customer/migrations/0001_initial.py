# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=b'50', verbose_name=b'customerName')),
                ('surname', models.CharField(max_length=b'50', verbose_name=b'customerSurname')),
                ('birth_date', models.DateTimeField()),
                ('email', models.CharField(max_length=b'30', verbose_name=b'customerEmail')),
                ('country', models.CharField(max_length=b'50', verbose_name=b'customerCountry')),
                ('city', models.CharField(max_length=b'50', verbose_name=b'customerCity')),
                ('address', models.CharField(max_length=b'100', verbose_name=b'customerAddress')),
                ('homePhone', models.IntegerField(verbose_name=b'customerHomePhone')),
                ('mobilePhone', models.IntegerField(verbose_name=b'customerMobilePhone')),
                ('added', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('customer', models.ForeignKey(to='customer.Customer', to_field='id')),
                ('meetingType', models.CharField(max_length=b'20', verbose_name=b'meetingType')),
                ('meetingDate', models.DateTimeField(auto_now=True)),
                ('meetingProject', models.CharField(max_length=b'30', verbose_name=b'meetingProject')),
                ('meetingComment', models.CharField(max_length=b'50', verbose_name=b'meetingComment')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
