# Generated by Django 4.1 on 2023-02-24 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("rental_store", "0008_rename_state_shippingaddress_county"),
    ]

    operations = [
        migrations.RenameField(
            model_name="shippingaddress",
            old_name="county",
            new_name="state",
        ),
        migrations.RemoveField(
            model_name="shippingaddress",
            name="phone_number",
        ),
    ]