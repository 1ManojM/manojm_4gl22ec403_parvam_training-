# Generated by Django 5.1.7 on 2025-03-25 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('phone', models.CharField(max_length=10, unique=True)),
                ('email', models.CharField(max_length=50)),
                ('quallification', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=50)),
                ('experience', models.IntegerField()),
            ],
        ),
    ]
