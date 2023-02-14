# Generated by Django 3.0.7 on 2020-06-19 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocer', '0003_remove_products_view'),
    ]

    operations = [
        migrations.CreateModel(
            name='latestproducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='pic')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('qty', models.CharField(max_length=10)),
                ('status', models.BooleanField(verbose_name=False)),
            ],
        ),
    ]