# Generated by Django 3.0.2 on 2020-03-23 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_mentor_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentor',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='profile_pics'),
        ),
        migrations.AddField(
            model_name='startup',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='profile_pics'),
        ),
    ]
