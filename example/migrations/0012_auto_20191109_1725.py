# Generated by Django 2.2.4 on 2019-11-09 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0011_ipstatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ipstatus',
            name='IP_ODconnect',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='ipstatus',
            name='IPconnect',
            field=models.CharField(max_length=10),
        ),
    ]