# Generated by Django 4.2.1 on 2023-06-04 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_gas_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gasstatus',
            name='percent',
            field=models.DecimalField(decimal_places=2, default=100, max_digits=3),
        ),
    ]
