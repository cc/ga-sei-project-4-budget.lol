# Generated by Django 2.2.7 on 2019-11-16 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('account_type', models.CharField(max_length=50)),
                ('bank', models.CharField(blank=True, max_length=50)),
                ('description', models.CharField(blank=True, max_length=500)),
                ('min_headroom', models.FloatField(blank=True, default=0)),
                ('current_balance', models.FloatField(null=True)),
                ('last_balance_update', models.DateField(blank=True)),
                ('is_main_account', models.BooleanField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FutureTransactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_is_debit', models.BooleanField()),
                ('name', models.CharField(max_length=50)),
                ('category', models.CharField(blank=True, max_length=50)),
                ('amount', models.FloatField()),
                ('recurrance', models.CharField(max_length=50)),
                ('day_of_week', models.CharField(blank=True, max_length=50)),
                ('date_in_month', models.IntegerField(null=True)),
                ('annual_date', models.DateField(blank=True)),
                ('one_off_date', models.DateField(blank=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='future_transactions', to='accounts.Account')),
            ],
        ),
    ]
