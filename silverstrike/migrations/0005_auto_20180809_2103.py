# Generated by Django 2.1 on 2018-08-09 21:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('silverstrike', '0004_auto_20180203_2257'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='digest',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
