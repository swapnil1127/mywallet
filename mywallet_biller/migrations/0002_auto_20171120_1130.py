# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-20 11:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mywallet_biller', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Biller',
            new_name='MyWalletBiller',
        ),
    ]
