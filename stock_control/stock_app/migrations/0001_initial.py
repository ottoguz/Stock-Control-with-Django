# Generated by Django 4.0 on 2023-02-14 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(default='', max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('cpf', models.CharField(max_length=15, unique=True)),
                ('creation_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]