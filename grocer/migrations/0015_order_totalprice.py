# Generated by Django 3.0.7 on 2020-07-21 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocer', '0014_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='totalPrice',
            field=models.CharField(default=0, max_length=999999),
            preserve_default=False,
        ),
    ]