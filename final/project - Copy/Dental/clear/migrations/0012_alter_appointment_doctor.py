# Generated by Django 4.2.6 on 2024-01-08 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clear', '0011_delete_registrationdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='doctor',
            field=models.CharField(choices=[('Dr. Coleen V. Lee, DMD', 'Dr. Coleen V. Lee, DMD'), ('Dr. Arleen Lim-Lee, DMD', 'Dr. Arleen Lim-Lee, DMD')], max_length=50),
        ),
    ]
