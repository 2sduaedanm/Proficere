# Generated by Django 3.2.12 on 2022-11-22 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instruct', '0019_remove_challenge_allowvideorecord'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='allowvideorecord',
            field=models.BooleanField(default=True),
        ),
    ]
