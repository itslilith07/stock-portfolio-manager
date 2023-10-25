# Generated by Django 4.2.1 on 2023-09-04 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DollarSign', '0004_stock_companyname_stock_symbol'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='marketCap',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='stock',
            name='peRatio',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='stock',
            name='previousClose',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='stock',
            name='week52High',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='stock',
            name='week52Low',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='stock',
            name='ytdChange',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]