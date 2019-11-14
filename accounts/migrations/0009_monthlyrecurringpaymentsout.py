# Generated by Django 2.2.7 on 2019-11-14 21:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20191114_1644'),
    ]

    operations = [
        migrations.CreateModel(
            name='MonthlyRecurringPaymentsOut',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('category', models.CharField(blank=True, max_length=50)),
                ('amount', models.FloatField(null=True)),
                ('date_in_month', models.IntegerField(null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='monthly_recurring_out', to='accounts.Account')),
            ],
        ),
    ]