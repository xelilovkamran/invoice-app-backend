# Generated by Django 5.0.7 on 2024-07-21 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0012_remove_invoice_identifier_invoice_uuid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='uuid',
        ),
        migrations.AddField(
            model_name='invoice',
            name='identifier',
            field=models.CharField(default=None, max_length=6, unique=True),
            preserve_default=False,
        ),
    ]
