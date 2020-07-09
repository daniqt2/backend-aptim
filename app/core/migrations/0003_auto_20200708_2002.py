# Generated by Django 2.1.15 on 2020-07-08 20:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200708_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='club',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='requests', to='core.Club'),
        ),
        migrations.AlterField(
            model_name='request',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='requests', to=settings.AUTH_USER_MODEL),
        ),
    ]