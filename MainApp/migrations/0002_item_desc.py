# Generated by Django 4.2.7 on 2023-11-22 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='desc',
            field=models.CharField(default=' ', max_length=256),
        ),
    ]
