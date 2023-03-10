# Generated by Django 4.1.1 on 2022-11-15 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_section_slug_alter_recipe_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='name',
            field=models.CharField(max_length=120),
        ),
        migrations.AddConstraint(
            model_name='section',
            constraint=models.UniqueConstraint(fields=('user', 'name'), name='unique name for each user'),
        ),
    ]
