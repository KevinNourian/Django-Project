# Generated by Django 3.2.5 on 2021-07-11 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plates', '0009_auto_20210711_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plate',
            name='letters',
            field=models.CharField(max_length=3, verbose_name='SKK'),
        ),
        migrations.AlterField(
            model_name='plate',
            name='numbers',
            field=models.CharField(max_length=3, verbose_name='660'),
        ),
    ]