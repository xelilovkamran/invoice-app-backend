# Generated by Django 5.0.7 on 2024-07-17 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0003_alter_invoice_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='post_code',
            new_name='postCode',
        ),
    ]
