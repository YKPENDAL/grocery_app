# Generated by Django 3.0.7 on 2020-06-27 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocer', '0010_remove_post_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='contact',
            field=models.IntegerField(max_length=10),
        ),
        migrations.AlterField(
            model_name='post',
            name='email',
            field=models.EmailField(max_length=255),
        ),
    ]
