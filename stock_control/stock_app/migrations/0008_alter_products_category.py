# Generated by Django 4.0 on 2023-03-02 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_app', '0007_alter_products_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.CharField(choices=[('Cell Phones', 'Cell Phones'), ('Appliances', 'Appliances'), ('Computer Parts', 'Comp Parts'), ('Furniture', 'Furniture')], max_length=50),
        ),
    ]
