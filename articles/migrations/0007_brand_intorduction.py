# Generated by Django 2.0.5 on 2018-05-30 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_auto_20180530_2206'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='intorduction',
            field=models.TextField(default=''),
        ),
    ]
