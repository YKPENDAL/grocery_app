# Generated by Django 3.0.7 on 2020-06-26 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocer', '0008_auto_20200619_1804'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('contact', models.IntegerField()),
                ('email', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('pincode', models.IntegerField()),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('status', models.BooleanField(verbose_name=True)),
            ],
        ),
    ]
