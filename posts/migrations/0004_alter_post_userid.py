# Generated by Django 4.2.7 on 2023-12-06 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_post_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='userId',
            field=models.IntegerField(),
        ),
    ]
