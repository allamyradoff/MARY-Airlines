# Generated by Django 4.1.4 on 2022-12-19 12:09

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_flightcheck'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=15, null=True, verbose_name='Banneryň üstindäki ýazgy')),
                ('image', models.ImageField(blank=True, null=True, upload_to='section/', verbose_name='Banner')),
                ('desc', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Bölümiň giňişleýin beýany')),
                ('cat', models.CharField(choices=[('HYZMATDAŞLARA', 'Hyzmatdaşlara'), ('HYZMATLAR', 'Hyzmatlar')], default='HYZMATDAŞLARA', max_length=15, verbose_name='Haýsy menýu degişli ?')),
            ],
            options={
                'verbose_name': 'Bölüm',
                'verbose_name_plural': 'Bölüm goşmak',
            },
        ),
        migrations.AlterField(
            model_name='flightcheck',
            name='name',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Banneryň üstindäki ýazgy'),
        ),
        migrations.CreateModel(
            name='PDF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True, verbose_name='Filyň ady')),
                ('file', models.FileField(blank=True, null=True, upload_to='', verbose_name='File ýuklemek')),
                ('section', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.section', verbose_name='Haýsy bölüme degişli')),
            ],
            options={
                'verbose_name': 'File',
                'verbose_name_plural': 'File ýuklemek ',
            },
        ),
    ]
