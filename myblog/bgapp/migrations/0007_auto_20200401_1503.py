# Generated by Django 2.2.8 on 2020-04-01 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bgapp', '0006_auto_20200330_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
