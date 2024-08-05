# Generated by Django 5.0.7 on 2024-07-17 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0004_rename_post_code_address_postcode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='invoice',
        ),
        migrations.AddField(
            model_name='invoice',
            name='items',
            field=models.ManyToManyField(to='invoice.item'),
        ),
    ]
