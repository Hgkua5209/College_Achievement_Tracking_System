# Generated by Django 4.2.5 on 2023-10-20 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tracking', '0005_advisor_password_advisor_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='MeritRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='merit_requests/')),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]
