# Generated by Django 3.0.8 on 2020-08-01 14:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.CharField(max_length=10000)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
