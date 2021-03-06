# Generated by Django 3.0.7 on 2021-09-15 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cto', '0033_auto_20210629_1830'),
    ]

    operations = [
        migrations.AddField(
            model_name='contratos',
            name='importeContratoconiva',
            field=models.FloatField(blank=True, null=True, verbose_name='Importe con IVA'),
        ),
        migrations.AddField(
            model_name='contratos',
            name='ivaContrato',
            field=models.FloatField(blank=True, default=0.16, null=True, verbose_name='IVA del contrato'),
        ),
        migrations.AddField(
            model_name='contratos',
            name='netoContrato',
            field=models.FloatField(blank=True, null=True, verbose_name='Importe Neto'),
        ),
        migrations.AddField(
            model_name='contratos',
            name='retisrContrato',
            field=models.FloatField(blank=True, null=True, verbose_name='Retención de ISR'),
        ),
        migrations.AddField(
            model_name='contratos',
            name='retivaContrato',
            field=models.FloatField(blank=True, default=0.1, null=True, verbose_name='Retención de IVA'),
        ),
    ]
