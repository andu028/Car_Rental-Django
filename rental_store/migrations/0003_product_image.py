# Generated by Django 4.1 on 2023-02-12 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rental_store", "0002_rename_ordercar_orderitem_rename_car_product"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
    ]
