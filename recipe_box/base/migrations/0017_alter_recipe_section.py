# Generated by Django 4.1.1 on 2022-11-22 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0016_alter_food_id_remove_recipe_section_recipe_section'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='section',
            field=models.ManyToManyField(to='base.section'),
        ),
    ]
