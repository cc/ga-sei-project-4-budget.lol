# Generated by Django 2.2.7 on 2019-11-17 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20191116_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='is_main_account',
            field=models.BooleanField(default=True, null=True),
        ),
    ]
