# Generated by Django 3.1.7 on 2021-03-24 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_brand'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='title',
        ),
    ]
