# Generated by Django 2.0.5 on 2018-05-31 20:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brand_admin', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brandadmin',
            name='user',
        ),
        migrations.DeleteModel(
            name='BrandAdmin',
        ),
    ]