# Generated by Django 3.1.7 on 2021-03-24 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_brand_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=300)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
    ]