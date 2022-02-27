# Generated by Django 4.0.2 on 2022-02-26 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        ('user', '0001_initial'),
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DebtSale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('created_date', models.DateField()),
                ('updated_date', models.DateField()),
                ('end_date', models.DateField()),
                ('debt', models.FloatField()),
                ('status', models.BooleanField()),
                ('paid_date', models.DateField()),
                ('id_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.client')),
                ('id_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.users')),
            ],
        ),
    ]
