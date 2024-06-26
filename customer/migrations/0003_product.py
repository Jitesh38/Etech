# Generated by Django 4.2.6 on 2024-03-28 11:33

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_category_subcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('pid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=125)),
                ('image', models.ImageField(upload_to='products/')),
                ('price', models.IntegerField()),
                ('srtdesc', models.CharField(max_length=225)),
                ('qty', models.IntegerField(default=50)),
                ('desc', models.TextField()),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.subcategory')),
            ],
        ),
    ]
