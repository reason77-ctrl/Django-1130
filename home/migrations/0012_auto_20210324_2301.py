# Generated by Django 3.1.7 on 2021-03-24 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='discript',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='address',
            name='subaddress',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='address',
            name='time',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='address',
            name='email',
            field=models.EmailField(blank=True, max_length=100),
        ),
    ]
