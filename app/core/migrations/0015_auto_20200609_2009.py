# Generated by Django 2.1.15 on 2020-06-09 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20200609_1434'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='votes',
        ),
        migrations.AddField(
            model_name='comment',
            name='votes',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='thread',
            name='likes',
        ),
        migrations.AddField(
            model_name='thread',
            name='likes',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
