# Generated by Django 4.0 on 2023-03-28 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_app', '0015_entry_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry_notes',
            name='supplier',
            field=models.CharField(choices=[('bosta', 'Suppliers')], max_length=50),
        ),
    ]
