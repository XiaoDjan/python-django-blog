# Generated by Django 2.2.1 on 2019-05-15 09:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0019_auto_20190515_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 15, 9, 55, 5, 28881, tzinfo=utc)),
        ),
    ]
