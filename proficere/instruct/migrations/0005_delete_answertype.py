# Generated by Django 3.1.5 on 2021-02-12 00:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instruct', '0004_remove_challenge_answertypeid'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AnswerType',
        ),
    ]