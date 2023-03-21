# Generated by Django 4.1.2 on 2022-10-29 10:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0010_decoration_fk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='decoration',
            name='fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterModelTable(
            name='decoration',
            table='decoration',
        ),
    ]
