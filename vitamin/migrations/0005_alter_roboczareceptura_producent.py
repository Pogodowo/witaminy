# Generated by Django 3.2.5 on 2021-11-27 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vitamin', '0004_roboczareceptura_producent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roboczareceptura',
            name='producent',
            field=models.TextField(blank=True, choices=[('1', 'producent 1'), ('2', 'producent 2')], null=True),
        ),
    ]
