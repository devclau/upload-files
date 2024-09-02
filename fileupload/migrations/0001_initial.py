# Generated by Django 5.0.6 on 2024-08-30 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_created=True)),
                ('nombre', models.CharField(blank=True, max_length=100)),
                ('file', models.FileField(max_length=200, upload_to='uploads/')),
            ],
        ),
    ]
