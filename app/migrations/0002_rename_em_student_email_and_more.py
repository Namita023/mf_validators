# Generated by Django 5.0.6 on 2024-08-13 05:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='em',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='sage',
            new_name='student_age',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='sid',
            new_name='student_id',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='sname',
            new_name='student_name',
        ),
    ]