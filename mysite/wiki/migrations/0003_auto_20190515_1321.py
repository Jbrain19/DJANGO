# Generated by Django 2.2 on 2019-05-15 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0002_useruploadfile'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserUploadfile',
            new_name='UserFileUpload',
        ),
    ]
