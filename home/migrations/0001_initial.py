# Generated by Django 3.1.2 on 2021-06-29 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pubg_registered_id',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('amount', models.CharField(max_length=100)),
                ('pubg_id', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('transactionid', models.CharField(max_length=100)),
                ('phone_4_digit', models.CharField(max_length=100)),
            ],
        ),
    ]
