# Generated by Django 3.0.7 on 2020-07-21 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocer', '0018_auto_20200721_2306'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='totalPrice',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
