# Generated by Django 3.1.13 on 2021-09-15 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0022_auto_20210915_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='pass_id',
            field=models.CharField(default=0, editable=False, max_length=20),
        ),
    ]
