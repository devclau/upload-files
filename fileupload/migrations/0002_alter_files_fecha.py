# Generated by Django 5.0.6 on 2024-09-01 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileupload', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='fecha',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
