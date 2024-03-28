# Generated by Django 4.2.4 on 2024-01-26 03:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0022_recipt_remove_payment_image_payment_recipts'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipt',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='recipt',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
