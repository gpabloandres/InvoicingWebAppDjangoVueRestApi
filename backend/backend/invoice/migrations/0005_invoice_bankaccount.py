# Generated by Django 4.2.3 on 2023-08-24 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0004_alter_invoice_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='bankaccount',
            field=models.CharField(blank=True, max_length=266, null=True),
        ),
    ]
