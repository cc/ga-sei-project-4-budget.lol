# Generated by Django 2.2.7 on 2019-11-13 23:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_currentaccount_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeeklyRecurringOut',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='weekly_recurring_out', to='accounts.CurrentAccount')),
            ],
        ),
    ]