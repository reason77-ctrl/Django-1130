# Generated by Django 3.1.7 on 2021-03-24 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_remove_brand_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='brand',
            old_name='image',
            new_name='images',
        ),
    ]