# Generated by Django 4.1.4 on 2022-12-15 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_airlinesservices_full_desc_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediasections',
            name='link',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Wideonyň ssylkasy'),
        ),
    ]
