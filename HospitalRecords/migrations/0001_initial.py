# Generated by Django 3.1.7 on 2021-02-24 01:54

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.user')),
                ('dob', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=500)),
                ('gender', models.CharField(max_length=1)),
                ('contact', models.CharField(max_length=10)),
                ('available', models.CharField(max_length=1)),
                ('name', models.CharField(max_length=100)),
                ('speciality', models.CharField(max_length=500)),
                ('currentlocation', models.IntegerField()),
            ],
            options={
                'db_table': 'Doctor',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.user')),
                ('dob', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=500)),
                ('gender', models.CharField(max_length=1)),
                ('contact', models.CharField(max_length=10)),
                ('height', models.CharField(max_length=10)),
                ('weight', models.CharField(max_length=10)),
                ('bloodgroup', models.CharField(max_length=10)),
                ('medicalconditions', models.CharField(max_length=500)),
                ('alergiesandreactions', models.CharField(max_length=500)),
                ('ongoingmedications', models.CharField(max_length=500)),
                ('familyhistory', models.CharField(max_length=500)),
                ('emergencycontact', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'Patient',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
