# Generated by Django 4.1 on 2023-02-24 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rental_store", "0005_alter_product_price"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="air_conditioning",
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name="product",
            name="engine",
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name="product",
            name="gear_box",
            field=models.CharField(max_length=30, null=True),
        ),
    ]
