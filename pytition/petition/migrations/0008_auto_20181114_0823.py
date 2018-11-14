# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-11-14 07:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('petition', '0007_auto_20180924_1738_squashed_0029_auto_20181031_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='default_template',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='petition.PetitionTemplate', verbose_name='Default petition template'),
        ),
        migrations.AlterField(
            model_name='petitiontemplate',
            name='footer_text',
            field=tinymce.models.HTMLField(blank=True),
        ),
        migrations.AlterField(
            model_name='petitiontemplate',
            name='name',
            field=models.CharField(db_index=True, max_length=50, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='pytitionuser',
            name='default_template',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='petition.PetitionTemplate', verbose_name='Default petition template'),
        ),
        migrations.AlterIndexTogether(
            name='petitiontemplate',
            index_together=set([('id',)]),
        ),
    ]
