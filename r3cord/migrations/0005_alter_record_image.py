# Generated by Django 4.2.7 on 2023-11-13 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('r3cord', '0004_alter_record_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='image',
            field=models.ImageField(blank=True, upload_to='r3cord/%Y/%m/'),
        ),
    ]
