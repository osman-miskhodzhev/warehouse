# Generated by Django 4.2 on 2024-12-01 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_unit_options_alter_product_name_and_more'),
        ('shipping', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shipment',
            options={'verbose_name': 'Выгрузка'},
        ),
        migrations.AlterModelOptions(
            name='shippinginvoice',
            options={'verbose_name': 'Накладная на выгрузку'},
        ),
        migrations.AlterModelOptions(
            name='сounterparty',
            options={'verbose_name': 'Контрагенты'},
        ),
        migrations.AlterField(
            model_name='shipment',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='Товар'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='shippingInvoice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shipping.shippinginvoice', verbose_name='Накладная'),
        ),
        migrations.AlterField(
            model_name='shippinginvoice',
            name='conterparty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shipping.сounterparty', verbose_name='Контрагент'),
        ),
        migrations.AlterField(
            model_name='сounterparty',
            name='name',
            field=models.CharField(max_length=120, verbose_name='Название контрагента'),
        ),
    ]
