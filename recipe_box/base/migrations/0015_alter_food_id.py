# Generated by Django 4.1.2 on 2022-11-18 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_food_slug_alter_food_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
