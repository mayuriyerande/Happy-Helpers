# Generated by Django 4.1.2 on 2022-10-27 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_contact_customers_phone'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Customers',
        ),
    ]