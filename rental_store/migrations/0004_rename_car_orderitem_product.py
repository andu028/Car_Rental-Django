# Generated by Django 4.1 on 2023-02-12 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("rental_store", "0003_product_image"),
    ]

    operations = [
        migrations.RenameField(
            model_name="orderitem",
            old_name="car",
            new_name="product",
        ),
    ]
