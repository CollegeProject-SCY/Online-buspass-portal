# Generated by Django 3.2.6 on 2021-09-03 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0018_auto_20210903_1031'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicants',
            name='user_pass',
            field=models.FileField(blank=True, null=True, upload_to='passes/'),
        ),
    ]
