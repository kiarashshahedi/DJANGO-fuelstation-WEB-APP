# Generated by Django 5.0.6 on 2024-06-15 12:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fuelstation',
            name='gas_final_stock',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fuelstation',
            name='gasoline_final_stock',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='GasolineTank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tank_number', models.IntegerField()),
                ('final_stock', models.FloatField()),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stations.fuelstation')),
            ],
        ),
        migrations.CreateModel(
            name='GasTank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tank_number', models.IntegerField()),
                ('final_stock', models.FloatField()),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stations.fuelstation')),
            ],
        ),
    ]