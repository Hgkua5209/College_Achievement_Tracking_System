# Generated by Django 4.2.5 on 2023-11-07 07:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Tracking', '0006_meritrequest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advisor',
            name='password',
        ),
        migrations.RemoveField(
            model_name='advisor',
            name='username',
        ),
        migrations.AddField(
            model_name='advisor',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
