# Generated by Django 3.2.5 on 2021-08-27 01:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0066_auto_20201213_1539'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='securityanswer01',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='securityquestion01',
        ),
        migrations.DeleteModel(
            name='SecurityQuestion',
        ),
    ]