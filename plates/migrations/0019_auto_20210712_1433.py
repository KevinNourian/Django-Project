# Generated by Django 3.2.5 on 2021-07-12 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plates', '0018_auto_20210712_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plate',
            name='letters',
            field=models.CharField(default='Y7C', max_length=3),
        ),
        migrations.AlterField(
            model_name='plate',
            name='numbers',
            field=models.CharField(default='756', max_length=3),
        ),
    ]