# Generated by Django 4.1.2 on 2022-10-29 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_decoration_fk_alter_decoration_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='decoration',
            old_name='fk',
            new_name='Customer_Name',
        ),
    ]
