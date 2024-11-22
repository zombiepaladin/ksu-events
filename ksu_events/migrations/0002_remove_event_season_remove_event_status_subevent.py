# Generated by Django 5.1.3 on 2024-11-22 16:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ksu_events', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='season',
        ),
        migrations.RemoveField(
            model_name='event',
            name='status',
        ),
        migrations.CreateModel(
            name='SubEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='The time this record was created.')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='The last time this record was updated.')),
                ('subevent_name', models.CharField(max_length=500, unique=True)),
                ('subevent_start_date', models.DateTimeField()),
                ('subevent_end_date', models.DateTimeField(blank=True, null=True)),
                ('location', models.CharField(max_length=500)),
                ('parent_event', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ksu_events.event')),
            ],
            options={
                'unique_together': {('subevent_name', 'parent_event')},
            },
        ),
    ]