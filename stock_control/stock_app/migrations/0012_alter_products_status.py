# Generated by Django 4.0 on 2023-03-08 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_app', '0011_alter_products_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='status',
            field=models.BooleanField(default=False, verbose_name='Available'),
        ),
    ]
