# Generated by Django 3.2.6 on 2022-05-30 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ToDo', models.TextField(max_length=2000, unique=True)),
                ('status', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'ToDo',
                'verbose_name_plural': 'ToDo',
            },
        ),
    ]
