# Generated by Django 3.0.7 on 2020-08-13 16:45

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_userforeignkey.models.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cto', '0003_auto_20200810_1951'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tipocontrato',
            name='docto01',
        ),
        migrations.RemoveField(
            model_name='tipocontrato',
            name='docto02',
        ),
        migrations.RemoveField(
            model_name='tipocontrato',
            name='docto03',
        ),
        migrations.RemoveField(
            model_name='tipocontrato',
            name='docto04',
        ),
        migrations.RemoveField(
            model_name='tipocontrato',
            name='docto05',
        ),
        migrations.RemoveField(
            model_name='tipocontrato',
            name='docto06',
        ),
        migrations.RemoveField(
            model_name='tipocontrato',
            name='docto07',
        ),
        migrations.RemoveField(
            model_name='tipocontrato',
            name='docto08',
        ),
        migrations.RemoveField(
            model_name='tipocontrato',
            name='docto09',
        ),
        migrations.RemoveField(
            model_name='tipocontrato',
            name='docto10',
        ),
        migrations.RemoveField(
            model_name='tipocontrato',
            name='docto11',
        ),
        migrations.RemoveField(
            model_name='tipocontrato',
            name='docto12',
        ),
        migrations.RemoveField(
            model_name='tipocontrato',
            name='docto13',
        ),
        migrations.RemoveField(
            model_name='tipocontrato',
            name='docto14',
        ),
        migrations.RemoveField(
            model_name='tipocontrato',
            name='docto15',
        ),
        migrations.RemoveField(
            model_name='tipocontrato',
            name='docto16',
        ),
        migrations.CreateModel(
            name='Requisitos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('requisito', models.CharField(max_length=150, verbose_name='Documento')),
                ('coment_req', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Descripci??n')),
                ('indiya', models.BooleanField(default=False, verbose_name='Entregado')),
                ('tipocontrato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cto.Tipocontrato')),
                ('uc', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('um', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Requisito',
                'verbose_name_plural': 'Requisitos',
            },
        ),
    ]
