# Generated by Django 3.0.7 on 2020-07-10 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocer', '0011_auto_20200627_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='type',
            field=models.CharField(default='v', max_length=10),
        ),
    ]
