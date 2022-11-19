# Generated by Django 4.1.1 on 2022-09-29 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('emp_id', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
                ('working', models.BooleanField()),
                ('department', models.CharField(max_length=200)),
            ],
        ),
    ]
