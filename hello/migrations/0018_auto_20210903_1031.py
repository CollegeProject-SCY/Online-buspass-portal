# Generated by Django 3.2.6 on 2021-09-03 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0017_auto_20210903_1027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicants',
            name='expire_date',
        ),
        migrations.AddField(
            model_name='transaction',
            name='expire_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
