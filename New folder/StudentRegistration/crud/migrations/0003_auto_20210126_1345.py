# Generated by Django 3.1.4 on 2021-01-26 08:15

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_auto_20210126_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='id',
            field=models.IntegerField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
