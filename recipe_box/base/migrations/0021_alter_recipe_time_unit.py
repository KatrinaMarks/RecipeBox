# Generated by Django 4.1.1 on 2022-11-27 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0020_recipe_time_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='time_unit',
            field=models.CharField(default='minutes', max_length=10),
        ),
    ]
