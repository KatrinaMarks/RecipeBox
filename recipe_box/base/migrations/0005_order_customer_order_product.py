# Generated by Django 4.1.1 on 2022-11-14 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_order_alter_recipe_section'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.CharField(default=0, max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.CharField(default=0, max_length=120),
            preserve_default=False,
        ),
    ]
