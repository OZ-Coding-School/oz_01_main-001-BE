# Generated by Django 5.0.6 on 2024-05-27 08:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('ingredient_id', models.AutoField(max_length=20, primary_key=True, serialize=False)),
                ('ingredient_name', models.CharField(max_length=100)),
                ('ingredient_type', models.CharField(max_length=100)),
                ('expiration_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('menu_id', models.AutoField(primary_key=True, serialize=False)),
                ('menu_name', models.CharField(max_length=30)),
                ('ingredient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fridge.ingredient')),
            ],
        ),
        migrations.CreateModel(
            name='IngredientMenuMapping',
            fields=[
                ('mapping_id', models.AutoField(primary_key=True, serialize=False)),
                ('ingredient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fridge.ingredient')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fridge.menu')),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('recipe_id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.TextField()),
                ('calories', models.FloatField()),
                ('ingredient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fridge.ingredient')),
                ('mapping', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fridge.ingredientmenumapping')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fridge.menu')),
            ],
        ),
    ]
