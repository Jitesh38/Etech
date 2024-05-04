# Generated by Django 5.0.3 on 2024-05-01 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0023_alter_cacnceledorder_reason'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerorder',
            name='payment',
            field=models.CharField(choices=[('COD', 'Cash on Delivery'), ('Done', 'Done')], default='COD', max_length=20),
        ),
    ]
