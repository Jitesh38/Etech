# Generated by Django 5.0.3 on 2024-04-02 09:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0009_order'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='customerOrder',
            fields=[
                ('orderId', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=255)),
                ('itemjson', models.CharField(max_length=3000)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=1000)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('pincode', models.IntegerField()),
                ('phone', models.CharField(max_length=15)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='addcart',
            name='product',
        ),
        migrations.RemoveField(
            model_name='addcart',
            name='user',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='orders',
        ),
        migrations.DeleteModel(
            name='addCart',
        ),
    ]
