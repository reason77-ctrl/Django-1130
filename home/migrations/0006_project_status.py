# Generated by Django 3.1.7 on 2021-03-24 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_project_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='status',
            field=models.CharField(blank=True, choices=[('active', 'active'), ('', 'default')], max_length=100),
        ),
    ]
