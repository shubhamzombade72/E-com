# Generated by Django 5.1 on 2025-01-10 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0002_remove_order_order_id_order_payment_method_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='customer_email',
            field=models.EmailField(blank=True, max_length=255, null=True),
        ),
    ]
