# Generated by Django 3.2 on 2021-08-02 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0003_product_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='real_price',
            field=models.IntegerField(default=0),
        ),
    ]
