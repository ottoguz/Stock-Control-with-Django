# Generated by Django 4.0 on 2023-03-21 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_app', '0013_suppliers_alter_customers_cpf_alter_products_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suppliers',
            name='status',
            field=models.BooleanField(default=False, verbose_name='Status: Inactive / Active'),
        ),
    ]
