# Generated by Django 5.0.3 on 2024-04-30 07:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0014_coupencode_discount'),
    ]

    operations = [
        migrations.CreateModel(
            name='updateStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='', max_length=300, null=True)),
                ('orderId', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.customerorder')),
            ],
        ),
    ]
