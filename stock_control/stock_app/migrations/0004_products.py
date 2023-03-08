# Generated by Django 4.0 on 2023-02-26 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_app', '0003_delete_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('category', models.CharField(choices=[('C', 'Cell Phones'), ('A', 'Appliances'), ('P', 'Computer Parts'), ('P', 'Furniture')], max_length=1)),
            ],
        ),
    ]
