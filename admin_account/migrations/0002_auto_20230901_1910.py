# Generated by Django 3.2.20 on 2023-09-01 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(default='firstName', max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(default='lastName', max_length=50),
        ),
    ]
