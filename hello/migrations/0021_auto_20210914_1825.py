# Generated by Django 3.1.13 on 2021-09-14 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0020_auto_20210907_1449'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicants',
            name='reject',
        ),
        migrations.AddField(
            model_name='account',
            name='reject',
            field=models.BooleanField(default=False),
        ),
    ]
