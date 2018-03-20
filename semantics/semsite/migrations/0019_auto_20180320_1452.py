# Generated by Django 2.0.3 on 2018-03-20 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('semsite', '0018_handbookarticle_chapters'),
    ]

    operations = [
        migrations.AlterField(
            model_name='handbookarticle',
            name='chapters',
            field=models.TextField(help_text="Названия разделов должны писаться через $ и пробел, например 'Глава 1$ Глава 2'", verbose_name='Оглавление'),
        ),
    ]