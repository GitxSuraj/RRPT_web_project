# Generated by Django 3.2 on 2021-08-04 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0006_rename_name_contact_user_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='contact',
            new_name='Contact_us',
        ),
    ]