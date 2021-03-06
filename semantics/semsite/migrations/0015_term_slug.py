# Generated by Django 2.0.3 on 2018-03-18 16:04

import autoslug.fields
from django.db import migrations
import semsite.models

def migrate_data_forward(apps, schema_editor):
    for instance in semsite.models.Term.objects.all():
        print("Generating slug for %s"%instance)
        instance.save()

def migrate_data_backward(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('semsite', '0014_remove_term_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='term',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from=semsite.models.Term.slugify, unique=True),
        ),
        migrations.RunPython(
            migrate_data_forward,
            migrate_data_backward,
        ),
    ]
