# Generated by Django 4.1.5 on 2023-01-28 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pledge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pledge_time', models.BooleanField()),
                ('comment', models.CharField(max_length=200)),
                ('pledge_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('goal', models.IntegerField()),
                ('image', models.URLField()),
                ('is_open', models.BooleanField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('project_date', models.DateField()),
                ('project_starttime', models.DateTimeField()),
                ('project_endtime', models.DateTimeField()),
                ('project_location', models.TextField()),
            ],
        ),
    ]
