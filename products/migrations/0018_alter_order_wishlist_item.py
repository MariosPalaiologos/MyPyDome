# Generated by Django 3.2.6 on 2021-08-26 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='wishlist_item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.wishlist'),
        ),
    ]