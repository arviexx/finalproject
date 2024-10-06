# Generated by Django 4.2.6 on 2023-12-13 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clear', '0009_alter_appointment_doctor_alter_appointment_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrationData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('confirm_password', models.CharField(max_length=100)),
            ],
        ),
    ]
