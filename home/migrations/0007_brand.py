# Generated by Django 3.1.7 on 2021-03-24 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_project_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.TextField()),
                ('title', models.CharField(max_length=100)),
            ],
        ),
    ]