# Generated by Django 4.0 on 2023-02-27 12:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('stock_app', '0005_alter_products_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='creation_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
