# Generated by Django 3.0.1 on 2020-01-09 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0009_top_lists_restaurant_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='top_lists_restaurant',
            name='image',
            field=models.URLField(max_length=2500),
        ),
    ]
