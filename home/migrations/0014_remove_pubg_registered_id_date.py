# Generated by Django 3.1.2 on 2021-07-05 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20210705_1502'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pubg_registered_id',
            name='date',
        ),
    ]
