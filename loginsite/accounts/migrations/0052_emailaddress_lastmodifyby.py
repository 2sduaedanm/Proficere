# Generated by Django 3.0.9 on 2020-09-09 04:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0051_emailtype_lastmodifyby'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailaddress',
            name='lastmodifyby',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]