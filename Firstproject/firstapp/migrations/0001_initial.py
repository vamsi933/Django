# Generated by Django 5.0 on 2023-12-20 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Iplmatches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('Headcoach', models.CharField(max_length=100)),
                ('captain', models.CharField(max_length=100)),
                ('no_of_Trophies', models.IntegerField()),
            ],
        ),
    ]
