# Generated by Django 4.1.2 on 2023-02-01 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_category_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='image',
        ),
    ]