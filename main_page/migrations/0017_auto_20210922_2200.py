# Generated by Django 3.2 on 2021-09-22 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0016_auto_20210907_2142'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='contact',
            name='desc_type',
            field=models.CharField(default='', max_length=25),
        ),
    ]
