# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2022-01-27 15:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('barth_day', models.DateField()),
                ('phone', models.CharField(max_length=13)),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('degree', models.FloatField()),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='result', to='human_resource.Level')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=55)),
                ('is_required', models.BooleanField()),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject', to='human_resource.Level')),
            ],
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='human_resource.Person')),
            ],
            bases=('human_resource.person',),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='human_resource.Person')),
                ('class_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student', to='human_resource.Class')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student', to='human_resource.Level')),
            ],
            bases=('human_resource.person',),
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='human_resource.Person')),
                ('classes_name', models.ManyToManyField(related_name='teacher', to='human_resource.Class')),
                ('levels', models.ManyToManyField(related_name='teacher', to='human_resource.Level')),
            ],
            bases=('human_resource.person',),
        ),
        migrations.AddField(
            model_name='result',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='result', to='human_resource.Subject'),
        ),
        migrations.AddField(
            model_name='person',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='human_resource.UserType'),
        ),
        migrations.AddField(
            model_name='result',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='result', to='human_resource.Student'),
        ),
        migrations.AddField(
            model_name='parent',
            name='children',
            field=models.ManyToManyField(related_name='parent', to='human_resource.Student'),
        ),
        migrations.AddField(
            model_name='parent',
            name='levels',
            field=models.ManyToManyField(related_name='parent', to='human_resource.Level'),
        ),
    ]