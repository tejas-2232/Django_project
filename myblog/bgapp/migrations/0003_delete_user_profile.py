# Generated by Django 2.2.8 on 2020-03-28 22:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bgapp', '0002_user_profile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User_profile',
        ),
    ]