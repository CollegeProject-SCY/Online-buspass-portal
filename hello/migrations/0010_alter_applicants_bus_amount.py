# Generated by Django 3.2.6 on 2021-08-31 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0009_applicants_bus_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicants',
            name='bus_amount',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
