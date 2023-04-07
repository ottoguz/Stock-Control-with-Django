# Generated by Django 4.0 on 2023-03-22 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_app', '0014_alter_suppliers_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry_notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier', models.CharField(choices=[], max_length=50)),
                ('date_time', models.DateTimeField()),
                ('value', models.FloatField(default=0.0)),
            ],
        ),
    ]