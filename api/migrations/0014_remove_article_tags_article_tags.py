# Generated by Django 5.1 on 2024-09-12 10:24

import taggit.managers
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_alter_about_content_alter_article_content_and_more'),
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='tags',
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
