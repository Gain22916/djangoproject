# Generated by Django 2.2.4 on 2020-02-10 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0014_daily_feeds'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daily_feeds',
            name='daily_name',
            field=models.CharField(max_length=40),
        ),
    ]
