# Generated by Django 4.0 on 2022-07-24 14:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0003_athlete_vote'),
    ]

    operations = [
        migrations.AddField(
            model_name='athlete',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 24, 14, 6, 21, 668260, tzinfo=utc), verbose_name='date published'),
            preserve_default=False,
        ),
    ]