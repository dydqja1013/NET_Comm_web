# Generated by Django 2.2.7 on 2019-12-05 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hyun', '0002_auto_20191205_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_hyun',
            name='author',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
