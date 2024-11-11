# Generated by Django 5.0.7 on 2024-11-11 18:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0013_remove_invoice_uuid_invoice_identifier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item', to='invoice.invoice'),
        ),
    ]