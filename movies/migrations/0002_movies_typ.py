# Generated by Django 5.0.4 on 2024-05-29 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='typ',
            field=models.CharField(default='action', max_length=200),
        ),
    ]
