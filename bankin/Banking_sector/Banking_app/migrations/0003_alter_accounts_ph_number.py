# Generated by Django 5.1 on 2024-08-08 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Banking_app', '0002_alter_accounts_account_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='ph_number',
            field=models.IntegerField(),
        ),
    ]
