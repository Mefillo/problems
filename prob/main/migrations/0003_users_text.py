# Generated by Django 2.2.4 on 2019-08-29 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20190829_1828'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='text',
            field=models.CharField(default='hui', max_length=200),
        ),
    ]
