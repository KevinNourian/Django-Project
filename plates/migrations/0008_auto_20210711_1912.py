# Generated by Django 3.2.5 on 2021-07-11 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plates', '0007_auto_20210711_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plate',
            name='letters',
            field=models.CharField(default='PRD', max_length=3),
        ),
        migrations.AlterField(
            model_name='plate',
            name='numbers',
            field=models.CharField(default='784', max_length=3),
        ),
    ]
