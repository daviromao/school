# Generated by Django 3.2.13 on 2022-05-11 23:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assessment',
            old_name='status',
            new_name='active',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='status',
            new_name='active',
        ),
    ]