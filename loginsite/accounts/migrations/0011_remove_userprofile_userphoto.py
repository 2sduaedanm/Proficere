# Generated by Django 2.0.10 on 2020-06-24 04:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20200624_0014'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='userphoto',
        ),
    ]
