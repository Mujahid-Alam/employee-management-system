# Generated by Django 4.1.1 on 2022-09-29 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0002_rename_student_emp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emp',
            name='emp_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='emp',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]
