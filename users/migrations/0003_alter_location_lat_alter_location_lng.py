# Generated by Django 4.1.4 on 2022-12-26 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_alter_location_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="location",
            name="lat",
            field=models.DecimalField(decimal_places=6, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name="location",
            name="lng",
            field=models.DecimalField(decimal_places=6, max_digits=8, null=True),
        ),
    ]
