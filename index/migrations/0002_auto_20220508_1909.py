# Generated by Django 2.2 on 2022-05-08 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trackin',
            name='slug',
            field=models.SlugField(blank=b'I01\n'),
        ),
        migrations.AlterField(
            model_name='trackin',
            name='Tracking_ID',
            field=models.CharField(max_length=15),
        ),
    ]