# Generated by Django 4.2.6 on 2023-10-27 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('time', models.DateTimeField()),
                ('amount_in_ml', models.IntegerField()),
                ('direction', models.CharField(choices=[('IN', 'went inside'), ('OUT', 'came outside')], default='IN', max_length=3)),
                ('note', models.TextField()),
                ('image', models.ImageField(upload_to='r3cord/%Y/%m/%d/')),
            ],
        ),
    ]
