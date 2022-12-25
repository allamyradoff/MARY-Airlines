# Generated by Django 4.1.4 on 2022-12-15 12:57

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_bannerforairlinesservices'),
    ]

    operations = [
        migrations.CreateModel(
            name='AirlinesServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250, null=True, verbose_name='Gullugyň ady')),
                ('image', models.ImageField(blank=True, null=True, upload_to='airlines_services/', verbose_name='Gullugyň suraty')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Gulluk',
                'verbose_name_plural': 'H.M gulluklar bölümi',
            },
        ),
        migrations.AlterModelOptions(
            name='bannerforairlinesservices',
            options={'verbose_name': 'Banner', 'verbose_name_plural': 'H.M gulluklar bölümindäki banner'},
        ),
    ]
