# Generated by Django 3.0.9 on 2020-09-09 05:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0056_auto_20200909_0006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='lastmodifyby',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='Countrymodifier', to=settings.AUTH_USER_MODEL),
        ),
    ]
