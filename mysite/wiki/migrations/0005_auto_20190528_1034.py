# Generated by Django 2.2 on 2019-05-28 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0004_counter'),
    ]

    operations = [
        migrations.DeleteModel(
            name='counter',
        ),
        migrations.AddField(
            model_name='page',
            name='counter',
            field=models.IntegerField(default=1),
        ),
    ]