# Generated by Django 4.2.6 on 2024-03-28 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0006_alter_category_parent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subcategory',
            old_name='parent',
            new_name='category',
        ),
        migrations.RemoveField(
            model_name='category',
            name='level',
        ),
        migrations.RemoveField(
            model_name='category',
            name='lft',
        ),
        migrations.RemoveField(
            model_name='category',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='category',
            name='rght',
        ),
        migrations.RemoveField(
            model_name='category',
            name='tree_id',
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='level',
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='lft',
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='rght',
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='tree_id',
        ),
    ]
