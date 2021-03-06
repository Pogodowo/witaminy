# Generated by Django 3.2.5 on 2021-08-30 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vitamin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='roboczareceptura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skladnik', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Skladnikrecepty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwas', models.CharField(max_length=30)),
                ('ilegramliqs', models.DecimalField(blank=True, decimal_places=3, max_digits=6)),
                ('ilejms', models.DecimalField(blank=True, decimal_places=3, max_digits=6)),
                ('ilegrams', models.DecimalField(blank=True, decimal_places=3, max_digits=6)),
                ('ilekroplis', models.DecimalField(blank=True, decimal_places=3, max_digits=6)),
                ('ilemls', models.DecimalField(blank=True, decimal_places=3, max_digits=6)),
                ('ileops', models.DecimalField(blank=True, decimal_places=3, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='ElementyFormularzaSkladnika',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jednostkawit', models.TextField(choices=[('1', 'g liq.'), ('2', 'j.m.'), ('3', 'op'), ('4', 'krople'), ('5', 'ml'), ('5', 'g')])),
                ('ilosc', models.DecimalField(blank=True, decimal_places=3, max_digits=6)),
                ('skladnik', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vitamin.skladnik')),
            ],
        ),
    ]
