# Generated by Django 3.2.3 on 2021-05-16 19:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_linkpost_total_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='linkpost',
            name='total_likes',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]