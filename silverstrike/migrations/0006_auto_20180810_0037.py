# Generated by Django 2.1 on 2018-08-10 00:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('silverstrike', '0005_auto_20180809_2103'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='fitid',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
    ]
