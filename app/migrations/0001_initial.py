# Generated by Django 5.0.6 on 2024-08-13 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('sid', models.IntegerField(primary_key=True, serialize=False)),
                ('sname', models.CharField(max_length=100)),
                ('sage', models.IntegerField()),
                ('em', models.EmailField(max_length=254)),
            ],
        ),
    ]
