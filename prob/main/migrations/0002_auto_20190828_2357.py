# Generated by Django 2.2.4 on 2019-08-28 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='problem',
            name='num',
        ),
        migrations.AddField(
            model_name='problem',
            name='number',
            field=models.IntegerField(default=0, unique=True),
        ),
    ]
