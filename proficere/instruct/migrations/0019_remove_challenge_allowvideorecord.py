# Generated by Django 3.2.12 on 2022-11-22 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instruct', '0018_alter_challenge_allowvideorecord'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='challenge',
            name='allowvideorecord',
        ),
    ]
