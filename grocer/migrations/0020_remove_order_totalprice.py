# Generated by Django 3.0.7 on 2020-07-21 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grocer', '0019_order_totalprice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='totalPrice',
        ),
    ]
