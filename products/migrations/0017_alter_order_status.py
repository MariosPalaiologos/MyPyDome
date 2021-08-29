# Generated by Django 3.2.6 on 2021-08-25 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending Approval', 'Pending Approval'), ('Out of Stock', 'Out of Stock'), ('Ordered', 'Ordered'), ('Delivering', 'Delivering'), ('Delivered', 'Delivered')], default='Pending Approval', max_length=200),
        ),
    ]