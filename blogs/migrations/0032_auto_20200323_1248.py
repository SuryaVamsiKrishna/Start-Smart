# Generated by Django 3.0.1 on 2020-03-23 07:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0031_auto_20200323_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 3, 23, 12, 48, 35, 909527)),
        ),
    ]
