# Generated by Django 3.2.5 on 2021-07-12 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plates', '0015_auto_20210711_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plate',
            name='letters',
            field=models.CharField(default='MSR', max_length=3),
        ),
        migrations.AlterField(
            model_name='plate',
            name='numbers',
            field=models.CharField(default='332', max_length=3),
        ),
    ]
