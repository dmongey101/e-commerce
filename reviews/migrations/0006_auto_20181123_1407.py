# Generated by Django 2.0.8 on 2018-11-23 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_reviews_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='rating',
            field=models.IntegerField(default=0, max_length=5),
        ),
    ]
