# Generated by Django 4.2.6 on 2024-03-10 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EtechApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='message',
        ),
        migrations.AddField(
            model_name='contact',
            name='desc',
            field=models.TextField(default='', max_length=300),
        ),
    ]
