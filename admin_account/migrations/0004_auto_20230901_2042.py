# Generated by Django 3.2.20 on 2023-09-01 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_account', '0003_auto_20230901_1950'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='website',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='username',
            field=models.CharField(default='name', max_length=24),
        ),
    ]
