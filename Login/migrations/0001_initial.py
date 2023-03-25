# Generated by Django 4.1.7 on 2023-03-23 18:49

import Login.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User_class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=50)),
                ('designation', models.CharField(choices=[('Student', 'Student'), ('Hall Manager', 'Hall Manager'), ('Mess Manager', 'Mess Manager'), ('Canteen Manager', 'Canteen Manager'), ('Sports Secy', 'Sports Secy')], max_length=15)),
                ('username', models.CharField(blank=True, max_length=20, unique=True)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', Login.models.UserManager()),
            ],
        ),
    ]
