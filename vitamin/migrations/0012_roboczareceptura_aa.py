# Generated by Django 3.2.5 on 2021-12-09 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vitamin', '0011_roboczareceptura_ilosc_na_recepcie'),
    ]

    operations = [
        migrations.AddField(
            model_name='roboczareceptura',
            name='aa',
            field=models.BooleanField(default=False),
        ),
    ]
