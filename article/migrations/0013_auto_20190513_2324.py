# Generated by Django 2.2.1 on 2019-05-13 15:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0012_auto_20190513_2302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 13, 15, 24, 56, 178879, tzinfo=utc)),
        ),
    ]