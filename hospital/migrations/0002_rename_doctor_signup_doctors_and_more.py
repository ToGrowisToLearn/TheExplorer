# Generated by Django 5.0.1 on 2024-03-05 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Doctor_Signup',
            new_name='Doctors',
        ),
        migrations.RenameModel(
            old_name='Patient_Signup',
            new_name='Patients',
        ),
        migrations.AlterModelTable(
            name='doctors',
            table='Doctors',
        ),
        migrations.AlterModelTable(
            name='patients',
            table='Patients',
        ),
    ]
