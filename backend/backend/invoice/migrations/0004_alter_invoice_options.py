# Generated by Django 4.2.3 on 2023-08-24 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0003_invoice_is_paid'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='invoice',
            options={'ordering': ('-created_at',)},
        ),
    ]
