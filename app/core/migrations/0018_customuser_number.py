# Generated by Django 2.1.15 on 2020-06-11 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_auto_20200610_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='number',
            field=models.CharField(blank=True, max_length=9, null=True),
        ),
    ]