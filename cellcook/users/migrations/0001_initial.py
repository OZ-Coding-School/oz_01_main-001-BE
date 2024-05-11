# Generated by Django 5.0.4 on 2024-05-11 04:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('nickname', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=255, null=True, unique=True, validators=[django.core.validators.EmailValidator(message='Enter a valid email address.')], verbose_name='email address')),
                ('password', models.CharField(max_length=100)),
                ('vegetarian', models.BooleanField(default=False)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
