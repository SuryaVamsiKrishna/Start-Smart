# Generated by Django 3.0.2 on 2020-03-06 16:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0013_auto_20200303_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 3, 6, 21, 39, 4, 322370)),
        ),
    ]
