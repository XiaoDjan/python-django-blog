# Generated by Django 2.2.1 on 2019-05-13 10:07

import datetime
from django.conf import settings
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0007_auto_20190512_2337'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlepost',
            name='users_like',
            field=models.ManyToManyField(blank=True, related_name='articles_like', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='articlepost',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 13, 10, 7, 30, 953296, tzinfo=utc)),
        ),
    ]
