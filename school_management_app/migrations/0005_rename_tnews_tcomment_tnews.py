# Generated by Django 3.2 on 2021-04-27 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school_management_app', '0004_auto_20210428_0151'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tcomment',
            old_name='Tnews',
            new_name='TNews',
        ),
    ]