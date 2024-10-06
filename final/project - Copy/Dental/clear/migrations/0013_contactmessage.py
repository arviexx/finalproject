# Generated by Django 4.2.6 on 2024-01-12 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clear', '0012_alter_appointment_doctor'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
    ]
