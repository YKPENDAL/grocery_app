# Generated by Django 3.0.7 on 2020-06-19 08:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grocer', '0004_latestproducts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='latestproducts',
            name='status',
        ),
    ]