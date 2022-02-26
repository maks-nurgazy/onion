# Generated by Django 4.0.2 on 2022-02-26 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=20)),
                ('firstName', models.CharField(max_length=30)),
                ('lastName', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=13)),
                ('password', models.CharField(max_length=30)),
                ('registrationDate', models.DateField()),
            ],
        ),
    ]
