# Generated by Django 5.0.7 on 2024-12-23 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0018_remove_item_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='total',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=10),
            preserve_default=False,
        ),
    ]
