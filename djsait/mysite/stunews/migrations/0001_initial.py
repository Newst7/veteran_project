# Generated by Django 4.1.5 on 2023-01-26 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('name', models.CharField(max_length=15)),
                ('fam', models.CharField(max_length=25)),
                ('otch', models.CharField(max_length=25)),
                ('url_photo', models.CharField(max_length=255)),
                ('news_data', models.DateField()),
            ],
        ),
    ]
