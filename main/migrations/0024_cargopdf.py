# Generated by Django 4.1.4 on 2022-12-16 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_cargo'),
    ]

    operations = [
        migrations.CreateModel(
            name='CargoPDF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to='', verbose_name='File ýuklemek')),
            ],
            options={
                'verbose_name': 'File',
                'verbose_name_plural': 'File ýuklemek "Goşlary geçirmegiň düzgünleri" ',
            },
        ),
    ]
