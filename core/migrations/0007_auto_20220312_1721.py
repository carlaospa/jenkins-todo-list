# Generated by Django 2.1.7 on 2022-03-12 20:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20220312_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 3, 12, 17, 21, 23, 989703)),
        ),
    ]
