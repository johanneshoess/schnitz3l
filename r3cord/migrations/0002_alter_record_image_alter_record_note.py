# Generated by Django 4.2.6 on 2023-10-27 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('r3cord', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='image',
            field=models.ImageField(blank=True, upload_to='r3cord/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='record',
            name='note',
            field=models.TextField(blank=True),
        ),
    ]
