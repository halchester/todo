# Generated by Django 3.1.3 on 2020-11-30 05:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='created_on',
        ),
    ]
