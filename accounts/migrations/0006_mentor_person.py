# Generated by Django 3.0.2 on 2020-03-08 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_mentor'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentor',
            name='person',
            field=models.IntegerField(default=0),
        ),
    ]
