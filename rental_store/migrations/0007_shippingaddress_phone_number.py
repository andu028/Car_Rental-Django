# Generated by Django 4.1 on 2023-02-24 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rental_store", "0006_product_air_conditioning_product_engine_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="shippingaddress",
            name="phone_number",
            field=models.CharField(max_length=200, null=True),
        ),
    ]
