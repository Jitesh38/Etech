# Generated by Django 5.0.3 on 2024-04-29 11:17

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0011_remove_customerorder_itemjson_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='coupenCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('open_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('expire_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.RemoveField(
            model_name='customerorder',
            name='productDetails',
        ),
        migrations.AlterField(
            model_name='customerorder',
            name='firstname',
            field=models.CharField(max_length=100, verbose_name='First name'),
        ),
        migrations.AlterField(
            model_name='customerorder',
            name='lastname',
            field=models.CharField(max_length=100, verbose_name='Last name'),
        ),
        migrations.AlterField(
            model_name='customerorder',
            name='totalprice',
            field=models.IntegerField(verbose_name='Total Price'),
        ),
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='product',
            name='qty',
            field=models.IntegerField(default=50, verbose_name='Quantity'),
        ),
        migrations.AlterField(
            model_name='product',
            name='srtdesc',
            field=models.CharField(max_length=225, verbose_name='Short Description'),
        ),
        migrations.AddField(
            model_name='customerorder',
            name='productdetails',
            field=models.TextField(default=django.utils.timezone.now, verbose_name='Product Details'),
            preserve_default=False,
        ),
    ]
