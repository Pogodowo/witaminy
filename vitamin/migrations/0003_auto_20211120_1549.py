# Generated by Django 3.2.5 on 2021-11-20 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vitamin', '0002_elementyformularzaskladnika_roboczareceptura_skladnikrecepty'),
    ]

    operations = [
        migrations.AddField(
            model_name='roboczareceptura',
            name='ale',
            field=models.CharField(default='0', max_length=40),
        ),
        migrations.AddField(
            model_name='roboczareceptura',
            name='dziadejos',
            field=models.CharField(default='0', max_length=40),
        ),
        migrations.AddField(
            model_name='roboczareceptura',
            name='janko',
            field=models.CharField(default='0', max_length=40),
        ),
        migrations.AddField(
            model_name='roboczareceptura',
            name='okejos',
            field=models.CharField(default='0', max_length=40),
        ),
        migrations.AddField(
            model_name='roboczareceptura',
            name='sianko',
            field=models.CharField(default='0', max_length=40),
        ),
        migrations.AddField(
            model_name='roboczareceptura',
            name='super',
            field=models.CharField(default='0', max_length=40),
        ),
        migrations.AddField(
            model_name='roboczareceptura',
            name='wale',
            field=models.CharField(default='0', max_length=40),
        ),
        migrations.AddField(
            model_name='roboczareceptura',
            name='wodziejos',
            field=models.CharField(default='0', max_length=40),
        ),
    ]
