# Generated by Django 2.2.3 on 2022-08-15 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20220815_0912'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
