# Generated by Django 2.1.15 on 2020-06-10 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20200610_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='likes',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
