# Generated by Django 3.1.2 on 2021-06-29 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pubg_registered_id',
            name='tournament_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
