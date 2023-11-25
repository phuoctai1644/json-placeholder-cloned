# Generated by Django 4.2.7 on 2023-11-25 03:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=255)),
                ('suite', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('zipcode', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('catchParse', models.CharField(max_length=255)),
                ('bs', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Geo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('website', models.CharField(max_length=255)),
                ('address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.address')),
                ('company', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.company')),
            ],
        ),
        migrations.AddField(
            model_name='address',
            name='geo',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.geo'),
        ),
    ]
