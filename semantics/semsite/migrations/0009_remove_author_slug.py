# Generated by Django 2.0.3 on 2018-03-17 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('semsite', '0008_author_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='slug',
        ),
    ]
