# Generated by Django 2.2.7 on 2020-04-11 23:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
