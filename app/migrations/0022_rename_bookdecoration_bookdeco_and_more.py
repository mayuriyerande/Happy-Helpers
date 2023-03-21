# Generated by Django 4.1.2 on 2022-10-30 09:47

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0021_remove_bookdecoration_address_bookdecoration_address'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BookDecoration',
            new_name='BookDeco',
        ),
        migrations.AlterField(
            model_name='decoration',
            name='cleaning',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='decoration',
            name='flat',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='decoration',
            name='materials',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
