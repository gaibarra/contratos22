# Generated by Django 3.0.7 on 2021-05-20 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cto', '0030_auto_20210518_2239'),
    ]

    operations = [
        migrations.AddField(
            model_name='partes',
            name='personaParte',
            field=models.PositiveSmallIntegerField(choices=[(1, 'PERSONA FÍSICA'), (2, 'PERSONA MORAL')], default=1, verbose_name='Tipo de persona'),
        ),
    ]
