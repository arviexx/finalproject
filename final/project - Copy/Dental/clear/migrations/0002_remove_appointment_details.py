# Generated by Django 4.2.7 on 2023-11-10 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clear', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='details',
        ),
    ]