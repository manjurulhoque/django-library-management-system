# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-12-02 14:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_borrow'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='sid',
            new_name='student_id',
        ),
    ]
