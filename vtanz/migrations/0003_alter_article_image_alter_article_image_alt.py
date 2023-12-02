# Generated by Django 4.2.7 on 2023-12-02 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vtanz', '0002_article_archived_alter_article_article_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, upload_to='vtanz/%Y/%m/', verbose_name='Bild'),
        ),
        migrations.AlterField(
            model_name='article',
            name='image_alt',
            field=models.CharField(blank=True, max_length=255, verbose_name='Bildbeschreibung'),
        ),
    ]
