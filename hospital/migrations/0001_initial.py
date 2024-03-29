# Generated by Django 5.0.1 on 2024-03-05 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor_Signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=25)),
                ('DID', models.IntegerField()),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('speciality', models.CharField(max_length=100)),
                ('mobile_no', models.BigIntegerField()),
                ('address', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Doctor_Signup',
            },
        ),
        migrations.CreateModel(
            name='Patient_Signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=25)),
                ('PID', models.IntegerField()),
                ('Age', models.IntegerField()),
                ('Gender', models.CharField(max_length=25)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('complaint', models.CharField(max_length=100)),
                ('consultation_area', models.CharField(max_length=100)),
                ('appointment_date_time', models.DateTimeField()),
                ('mobile_no', models.BigIntegerField()),
                ('address', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Patient_Signup',
            },
        ),
    ]
