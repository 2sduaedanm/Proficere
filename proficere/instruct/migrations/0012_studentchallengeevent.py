# Generated by Django 2.2.14 on 2021-04-09 03:28

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('instruct', '0011_auto_20210324_2020'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentChallengeEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assessdate', models.DateTimeField(default=datetime.datetime.now)),
                ('resultcode', models.BooleanField(default=False)),
                ('challengeid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instruct.Challenge')),
                ('curriculumid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instruct.Curriculum')),
                ('instructorid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instructor_user', to=settings.AUTH_USER_MODEL)),
                ('progressionid', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='instruct.Progression')),
                ('studentid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]