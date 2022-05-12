# Generated by Django 2.2 on 2021-09-15 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=100)),
                ('number', models.IntegerField()),
                ('message', models.CharField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Trackin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tracking_ID', models.CharField(max_length=10)),
                ('Delivery_Date', models.DateTimeField()),
                ('Delivery_State', models.CharField(max_length=50)),
                ('Current_Location', models.CharField(max_length=50)),
            ],
        ),
    ]