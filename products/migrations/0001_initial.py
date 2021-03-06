# Generated by Django 2.0.8 on 2018-11-19 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=254)),
                ('brand', models.CharField(default='', max_length=50)),
                ('sku', models.CharField(default='', max_length=50)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='images')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('stock', models.IntegerField(default=0)),
            ],
        ),
    ]
