# Generated by Django 2.2.4 on 2019-08-28 22:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(null=True)),
                ('num', models.IntegerField(default=0, unique=True, verbose_name='Number')),
            ],
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(null=True)),
                ('num', models.IntegerField(default=0, unique=True, verbose_name='Number')),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Problem')),
            ],
        ),
    ]
