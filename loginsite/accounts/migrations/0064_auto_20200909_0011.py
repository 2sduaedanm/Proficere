# Generated by Django 3.0.9 on 2020-09-09 05:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0063_auto_20200909_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailaddress',
            name='lastmodifyby',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='EmailAddressmodifier', to=settings.AUTH_USER_MODEL),
        ),
    ]
