# Generated by Django 4.2.1 on 2023-09-04 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DollarSign', '0005_stock_marketcap_stock_peratio_stock_previousclose_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='marketCap',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
    ]
