# Generated by Django 2.0.5 on 2020-04-22 01:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FirstApp', '0002_auto_20200421_1844'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='Address',
        ),
        migrations.RemoveField(
            model_name='candidate',
            name='Contact',
        ),
    ]