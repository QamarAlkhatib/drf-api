# Generated by Django 4.0 on 2021-12-12 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snackpost', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated',
            field=models.DateTimeField(),
        ),
    ]
