# Generated by Django 4.1.2 on 2022-10-30 10:25

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0022_rename_bookdecoration_bookdeco_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BookDeco',
            new_name='Book_Deco',
        ),
    ]
