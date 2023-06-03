# Generated by Django 4.2.1 on 2023-06-02 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leetcode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('url', models.URLField()),
                ('duration', models.IntegerField()),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('status', models.CharField(max_length=255)),
                ('in_24_hours', models.BooleanField()),
            ],
        ),
    ]