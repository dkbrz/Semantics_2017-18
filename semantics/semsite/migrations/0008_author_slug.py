# Generated by Django 2.0.3 on 2018-03-17 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('semsite', '0007_remove_term_letter'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='slug',
            field=models.SlugField(default='default'),
            preserve_default=False,
        ),
    ]