# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2022-01-28 15:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('human_resource', '0002_auto_20220127_2259'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='class',
            options={'verbose_name': 'الفصل', 'verbose_name_plural': 'الفصل'},
        ),
        migrations.AlterModelOptions(
            name='level',
            options={'verbose_name': ' المستوي', 'verbose_name_plural': ' المستوي'},
        ),
        migrations.AlterModelOptions(
            name='parent',
            options={'verbose_name': 'الاباء', 'verbose_name_plural': 'الاباء'},
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': 'الشخص', 'verbose_name_plural': 'الشخص'},
        ),
        migrations.AlterModelOptions(
            name='result',
            options={'verbose_name': 'النتائج', 'verbose_name_plural': 'النتائج'},
        ),
        migrations.AlterModelOptions(
            name='subject',
            options={'verbose_name': 'المادة', 'verbose_name_plural': 'المادة'},
        ),
        migrations.AlterModelOptions(
            name='teacher',
            options={'verbose_name': 'المعلمين', 'verbose_name_plural': 'المعلمين'},
        ),
        migrations.AlterModelOptions(
            name='usertype',
            options={'verbose_name': 'نوع المستخدم', 'verbose_name_plural': 'نوع المستخدم'},
        ),
        migrations.AddField(
            model_name='teacher',
            name='subject',
            field=models.ForeignKey(default=22, on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to='human_resource.Subject'),
            preserve_default=False,
        ),
    ]
