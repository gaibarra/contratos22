# Generated by Django 3.0.7 on 2020-08-11 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cto', '0002_auto_20200720_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partes',
            name='rfc',
            field=models.CharField(blank=True, max_length=14, null=True, verbose_name='RFC'),
        ),
    ]