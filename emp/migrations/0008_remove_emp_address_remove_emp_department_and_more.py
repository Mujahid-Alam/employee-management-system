# Generated by Django 4.1.1 on 2022-09-30 03:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0007_remove_emp_emp_id_remove_emp_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emp',
            name='address',
        ),
        migrations.RemoveField(
            model_name='emp',
            name='department',
        ),
        migrations.RemoveField(
            model_name='emp',
            name='name',
        ),
        migrations.RemoveField(
            model_name='emp',
            name='working',
        ),
    ]
