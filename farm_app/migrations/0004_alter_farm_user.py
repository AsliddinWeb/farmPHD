# Generated by Django 5.1.4 on 2025-01-11 11:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm_app', '0003_farm_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='farm',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='farm', to=settings.AUTH_USER_MODEL, verbose_name='Kimga tegishli'),
        ),
    ]
