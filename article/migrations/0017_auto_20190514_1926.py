# Generated by Django 2.2.1 on 2019-05-14 11:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0016_auto_20190514_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 14, 11, 26, 6, 201464, tzinfo=utc)),
        ),
    ]
