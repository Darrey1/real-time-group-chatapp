# Generated by Django 4.2.5 on 2023-10-01 22:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatting', '0002_alter_message_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]