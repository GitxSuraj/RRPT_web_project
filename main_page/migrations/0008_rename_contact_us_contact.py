# Generated by Django 3.2 on 2021-08-04 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0007_rename_contact_contact_us'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contact_us',
            new_name='Contact',
        ),
    ]
