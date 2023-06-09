# Generated by Django 4.2.1 on 2023-06-09 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=70)),
                ('chainList', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Quest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('blurb', models.TextField()),
                ('task', models.TextField()),
                ('image', models.ImageField(upload_to='quest/% Y % m % d/')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=50)),
                ('takes', models.TextField(null=True)),
                ('chain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jagd.chain')),
            ],
        ),
        migrations.CreateModel(
            name='Take',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('answer', models.TextField(null=True)),
                ('image', models.ImageField(upload_to='take/% Y % m % d/')),
                ('quest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jagd.quest')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jagd.team')),
            ],
        ),
    ]
