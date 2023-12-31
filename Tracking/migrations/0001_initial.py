# Generated by Django 4.2.5 on 2023-10-16 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advisor',
            fields=[
                ('advisorId', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('advisorName', models.CharField(max_length=128)),
                ('advisorPhone', models.CharField(max_length=128)),
                ('advisorEmail', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='SportsClubs',
            fields=[
                ('sportClubsCode', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('sportClubsName', models.CharField(max_length=128)),
                ('sportClubsDescription', models.TextField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('studentId', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('studentName', models.CharField(max_length=128)),
                ('studentCourse', models.CharField(max_length=128)),
                ('studentPhone', models.CharField(max_length=128)),
                ('studentEmail', models.CharField(max_length=128)),
                ('studentAddress', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Achivement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session', models.TextField(max_length=128)),
                ('date', models.DateField(blank=True, null=True)),
                ('achivement', models.TextField(max_length=128)),
                ('merit', models.IntegerField(default=0)),
                ('advisorId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tracking.advisor')),
                ('sportClubsCode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tracking.sportsclubs')),
                ('studentId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tracking.student')),
            ],
        ),
    ]
